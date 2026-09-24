from fastapi import APIRouter

from api.dependencies import UserServiceDep, UserIdDep
from schemas import UserResponseSchema, UpdateUserSchema


router = APIRouter(tags=['Profile'])


@router.get('/me', response_model=UserResponseSchema)
async def get_me(user_id: UserIdDep, user_service: UserServiceDep) -> UserResponseSchema:
    
    return await user_service.get_user_by_id(user_id)
    
@router.post('/update', response_model=UserResponseSchema)
async def update_me(user_id: UserIdDep, user_service: UserServiceDep, data: UpdateUserSchema) -> UserResponseSchema:
    
    return await user_service.update_user(user_id, data)


@router.delete('/delete')
async def delete_me(user_id: UserIdDep, user_service: UserServiceDep) -> None:
    
    await user_service.delete_user(user_id)