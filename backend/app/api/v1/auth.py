from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import timedelta

from app.core.database import get_db
from app.core.security import get_password_hash, verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from app.models.models import User
from app.schemas.schemas import UserCreate, UserResponse, Token

router = APIRouter(tags=["Authentication"])

# 1. SIGNUP ENDPOINT: To register a new user
@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def signup(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    print("\n" + "="*40)
    print(f"1. FRONTEND SE AAYA PASSWORD: {user_in.password}")
    print(f"TYPE OF PASSWORD: {type(user_in.password)}")
    print("="*40 + "\n")

    # Check if email already exists in the database
    query = select(User).where(User.email == user_in.email)
    result = await db.execute(query)
    existing_user = result.scalar_one_or_none()
    
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="This email is already registered."
        )

    # Hash the password (we won't save plain text)
    raw_password = user_in.password
    hashed_password = get_password_hash(raw_password)

    # Create a new user object
    new_user = User(
        email=user_in.email,
        hashed_password=hashed_password
    )
    
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    
    return new_user


# 2. LOGIN ENDPOINT: Verify user and provide JWT token
@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: AsyncSession = Depends(get_db)
):
    # Find user in the database (username in OAuth2 form is the email)
    query = select(User).where(User.email == form_data.username)
    result = await db.execute(query)
    user = result.scalar_one_or_none()

    # User not found or password is incorrect
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Login successful! Generate token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        subject=user.email, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}