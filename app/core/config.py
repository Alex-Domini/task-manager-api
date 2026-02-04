from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


"""
Важно:

SYNC_DATABASE_URL — для Alembic (потом можно использовать, если понадобиться из кода)
ASYNC_DATABASE_URL — для приложения (FastAPI)
"""
SYNC_DATABASE_URL = f"sqlite:///{BASE_DIR}/task_manager.db"
ASYNC_DATABASE_URL = f"sqlite+aiosqlite:///{BASE_DIR}/task_manager.db"



SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60