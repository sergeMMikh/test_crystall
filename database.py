import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import text, create_engine
from config import settings

# Настройка синхронного двигателя
sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False,
    pool_size=5,
    max_overflow=10,
)

# Настройка асинхронного двигателя
async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False,
    pool_size=5,
    max_overflow=10,
)

async def get_async():
    # Использование подключения
    async with async_engine.connect() as conn:
        result = await conn.execute(text("SELECT VERSION()"))  # Используем text() для строки SQL
        # for row in result:
        #     print(f"Database version: {row[0]}")

        print(f'{result.first()=}')

asyncio.run(get_async())