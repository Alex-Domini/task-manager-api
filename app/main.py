from fastapi import FastAPI

from app.routers.task import router as task_router
from app.routers.user import router as user_router
from app.routers.auth import router as auth_router

app = FastAPI(title="Task Manager App")



@app.get("/")
def health():
    return {"status": "ok"}

app.include_router(task_router)
app.include_router(user_router)
app.include_router(auth_router)