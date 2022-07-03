import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
load_dotenv(f"{os.path.dirname(os.path.abspath(__file__))}/.env")

class AsyncDBSession:
    def __init__(self):
        self._session = None
        self._engine  = None
    
    def __getattr__(self, name):
        return getattr(self._session, name)
    
    async def init(self):
        self._engine = create_async_engine(
            os.getenv("DB_URL"),
            echo = True
        ),
        self._session = sessionmaker(
            self._engine, expire_on_commit=False, class_=AsyncSession()
        )()
    
    async def create_all(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


async_db_session = AsyncDBSession()