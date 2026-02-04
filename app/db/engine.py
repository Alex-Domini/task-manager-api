from sqlalchemy.ext.asyncio import create_async_engine
from app.core.config import ASYNC_DATABASE_URL

engine = create_async_engine(ASYNC_DATABASE_URL, echo=False)
