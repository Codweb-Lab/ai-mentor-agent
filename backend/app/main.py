from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.core.database import get_db

app = FastAPI(
    title="Codweb Lab AI Mentor Agent",
    description="API for AI Mentor Agent",
    version="1.0.0"
)

# health check and database testing endpoint
@app.get("/")
async def root(db: AsyncSession = Depends(get_db)):
    try:
        # test database connection
        await db.execute(text("SELECT 1"))
        db_status = "Connected"
    except Exception as e:
        db_status = f"Disconnected: {str(e)}"

    return {
        "status": "success",
        "project": "Codweb Lab AI Mentor",
        "database": db_status
    }