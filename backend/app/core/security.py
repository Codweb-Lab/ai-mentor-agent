from datetime import datetime, timedelta, timezone
from typing import Any, Union
from jose import jwt
from passlib.context import CryptContext
import os, sys, bcrypt
from dotenv import load_dotenv

load_dotenv()

# loading configuration from .env
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))


# 1. hashing the password
def get_password_hash(password: str) -> str:
    print("\n" + "!"*40)
    print(f"SECURITY.PY ME PAUNCHA PASSWORD: {password}")
    print(f"PASSWORD LENGTH: {len(password)}")
    print("!"*40 + "\n", file=sys.stderr)

    # 1. Change string password to bytes
    password_bytes = password.encode('utf-8')
    # 2. Generate salt
    salt = bcrypt.gensalt()
    # 3. Hash using bcrypt
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    # 4. Convert back to string and return
    return hashed_password.decode('utf-8')


# 2. matching the hashed password with the plain password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


# 3. creating JWT Access Token for user
def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # Token payload
    to_encode = {"exp": expire, "sub": str(subject)}

    # Generate token by signing with SECRET_KEY
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt