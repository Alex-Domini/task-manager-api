from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.db.engine import engine

AsyncSessionLocal = async_sessionmaker(bind=engine,
                            autoflush=False,
                            autocommit=False,
                            expire_on_commit=False,
                            class_=AsyncSession,
                            )
