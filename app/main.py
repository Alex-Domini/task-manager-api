from fastapi import FastAPI



from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.db.deps import get_db

from app.routers.task import router as task_router
from app.routers.user import router as user_router
from app.routers.auth import router as auth_router

app = FastAPI(title="Task Manager App")



@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/db-health")
async def db_health(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT 1"))
    value = result.scalar()
    return {"db": "ok", "value": value}

app.include_router(task_router)
app.include_router(user_router)
app.include_router(auth_router)