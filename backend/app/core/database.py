from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# loading environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# session maker to communicate with the database
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

# create a declarative base for our models
Base = declarative_base()

# handling database session
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()