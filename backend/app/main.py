from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.core.database import get_db
from app.api.v1.auth import router as auth_router # Importing auth router
import traceback, sys

app = FastAPI(
    title="Codweb Lab AI Mentor Agent",
    description="API for AI Mentor Agent",
    version="1.0.0"
)

# Include Auth router with /api/v1/auth prefix
app.include_router(auth_router, prefix="/api/v1", tags=["Authentication"])

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

@app.exception_handler(Exception)
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # This code will forcibly print the error to the terminal
    print("====== SERVER CRASH DETECTED ======", file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    print("===================================", file=sys.stderr)
    
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error", "error_message": str(exc)}
    )