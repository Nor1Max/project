from sqlalchemy.ext.asyncio import AsyncSession
from models import User
from sqlalchemy import select
from uuid import UUID

class UserRepository:
    
    def __init__(self, session: AsyncSession):
        self.session = session
        
        
    async def get_by_email(self, email: str) -> User | None:
        
        stmt = select(User).where(User.email == email)
        result = await self.session.execute(stmt)
        
        return result.scalar_one_or_none()
    
    
    async def get_by_id(self, user_id: UUID) -> User | None:
        return await self.session.get(User, user_id)
    
    
    async def create(self, user_data: dict) -> User:
        
        new_user = User(**user_data)
        
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        
        return new_user
    
    
    async def get_all(self) -> list[User]:
        stmt = select(User)
        result = await self.session.execute(stmt)
        
        return result.scalars().all()
    
    
    async def save(self, user: User) -> User:
        await self.session.commit()
        await self.session.refresh(user)
        
        return user
    
    
    async def delete(self, user: User) -> None:
        await self.session.delete(user)
        await self.session.commit()