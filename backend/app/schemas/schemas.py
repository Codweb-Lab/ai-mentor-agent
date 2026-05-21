from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

# Base Schema
class UserBase(BaseModel):
    email: EmailStr

# Signup Request
class UserCreate(UserBase):
    password: str = Field(..., min_length=8, description="Password must be at least 8 characters long")

# Response Schema
class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        # Convert SQLAlchemy models to Pydantic models
        from_attributes = True

# Token Schema
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None