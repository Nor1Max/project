from fastapi import Depends, APIRouter
from uuid import UUID
from api.dependencies import UserServiceDep, require_admin
from schemas import UpdateUserAdminSchema, UserResponseSchema


router = APIRouter(tags=['Admin'])


@router.get('/all', response_model=list[UserResponseSchema], dependencies=[Depends(require_admin)])
async def get_users_all(user_service: UserServiceDep) -> list[UserResponseSchema]:
    return await user_service.get_user_all()


@router.get('/{user_id}', response_model=UserResponseSchema, dependencies=[Depends(require_admin)])
async def get_user_by_id(user_service: UserServiceDep, user_id: UUID) -> UserResponseSchema:
    return await user_service.get_user_by_id(user_id)


@router.patch('/{user_id}', response_model=UserResponseSchema, dependencies=[Depends(require_admin)])
async def update_user_admin(user_service: UserServiceDep, user_id: UUID, data: UpdateUserAdminSchema) -> UserResponseSchema:
    return await user_service.update_user(user_id, data)


@router.delete('/{user_id}', dependencies=[Depends(require_admin)])
async def delete_user(user_service: UserServiceDep, user_id: UUID) -> dict:
    await user_service.delete_user(user_id)
    
    return {'message': 'User удален из системы'}