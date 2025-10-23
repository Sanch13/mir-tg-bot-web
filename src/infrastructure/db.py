from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from src.config import settings

Base = declarative_base()

_engine = None
_session_factory: async_sessionmaker[AsyncSession] | None = None


def init_db_engine() -> None:
    """
    Инициализация движка и session factory.
    Вызывается при старте приложения (например, в main.py).
    """
    global _engine, _session_factory
    if _engine is not None:
        return

    _engine = create_async_engine(
        url=settings.db.construct_sqlalchemy_url,
        future=True,
        echo=False,
        pool_pre_ping=True,
    )
    _session_factory = async_sessionmaker(
        bind=_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )


def get_session_factory() -> async_sessionmaker[AsyncSession]:
    """
    Возвращает фабрику сессий, гарантируя, что init_db_engine был вызван.
    """
    if _session_factory is None:
        raise RuntimeError(
            "Database engine is not initialized. Call init_db_engine() before using DB sessions."
        )
    return _session_factory


def get_engine():
    if _engine is None:
        raise RuntimeError("Database engine not initialized.")
    return _engine
