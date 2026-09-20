from sqlalchemy.ext.asyncio import AsyncSession
from models import RefreshToken
from sqlalchemy import select
from uuid import UUID


class RefreshTokenRepository:
    
    def __init__(self, session: AsyncSession):
        self.session = session
        
        
    async def create(self, token: str, user_id: UUID) -> RefreshToken:
        
        new_token = RefreshToken(
            token=token, 
            user_id=user_id
        )
        
        self.session.add(new_token)
        await self.session.commit()
        await self.session.refresh(new_token)
        
        return new_token
    
    
    async def get_by_token_and_user(self, token: str, user_id: UUID) -> RefreshToken | None:
        
        stmt = select(RefreshToken).where(
            RefreshToken.token == token,
            RefreshToken.user_id == user_id
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    
    async def delete(self, token: RefreshToken) -> None:
       
        await self.session.delete(token)
        await self.session.commit()
    