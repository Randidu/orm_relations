from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.testing import future

DATABASE_URL = "postgresql+asyncpg://postgres:admin@localhost:5432/institute_db"

engin = create_async_engine(
    DATABASE_URL,
    echo = False,# set to true if you want to see sql statement produce
    pool_pre_ping = True, # verify the connections in pool before using them
    future = True
)

async_session = async_sessionmaker(
    engin,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False
)
async  def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()