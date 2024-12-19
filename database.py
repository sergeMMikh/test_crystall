from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import text, create_engine
from config import settings

# Настройка синхронного двигателя
engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    pool_size=5,
    max_overflow=10,
)

# Использование подключения
with engine.connect() as conn:
    result = conn.execute(text("SELECT VERSION()"))  # Используем text() для строки SQL
    for row in result:
        print(f"Database version: {row[0]}")
