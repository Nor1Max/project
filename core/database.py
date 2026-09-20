from core import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from uuid import UUID, uuid4


engine = create_async_engine(settings.database_url)

new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        yield session
        
        
class Base(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)