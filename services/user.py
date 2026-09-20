from uuid import UUID
from repositories import UserRepository
from schemas import UpdateUserAdminSchema
from core import NotFoundError
from models import User


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo
    
    
    async def get_user_all(self) -> list[User]:
        return await self.user_repo.get_all()
    
    
    async def get_user_by_id(self, user_id: UUID) -> User:
        user = await self.user_repo.get_by_id(user_id)
        
        if user is None:
            raise NotFoundError('User')
        
        return user
    
    
    async def update_user(self, user_id: UUID, data: UpdateUserAdminSchema) -> User:
        user = await self.user_repo.get_by_id(user_id)
        
        if user is None:
            raise NotFoundError('User')
        
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(user, key, value)
            
        return await self.user_repo.save(user)
    
    
    async def delete_user(self, user_id: UUID) -> None:
        user = await self.user_repo.get_by_id(user_id)
        
        if user is None:
            raise NotFoundError('User')
        
        await self.user_repo.delete(user)