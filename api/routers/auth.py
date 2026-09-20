from fastapi import Response, APIRouter
from api.dependencies import RefreshTokenPayloadDep, CurrentRefreshTokenDep, AuthServiceDep
from schemas import CreateUserSchema, CreateUserResponseSchema, LoginUserSchema
from core import security



router = APIRouter(tags=['Auth'])

@router.post('/register', response_model=CreateUserResponseSchema)
async def registration(auth_service: AuthServiceDep, data: CreateUserSchema) -> CreateUserResponseSchema:

    return await auth_service.register_user(data)
    


@router.post('/login')
async def login(auth_service: AuthServiceDep, data: LoginUserSchema, response: Response) -> dict:
    
    access_token, refresh_token = await auth_service.login_user(data)
    
    security.set_access_cookies(access_token, response)
    security.set_refresh_cookies(refresh_token, response)
    
    return {'message': 'Вы успешно вошли в аккаунт'}


@router.post('/refresh')
async def access_token_refresh(auth_service: AuthServiceDep, payload: RefreshTokenPayloadDep, response: Response, _: CurrentRefreshTokenDep) -> dict:
    
    new_access_token = await auth_service.refresh_access_token(payload)
    
    security.set_access_cookies(new_access_token, response)
    
    return {'message': 'access token обновлен'}


@router.post('/logout')
async def logout(auth_service: AuthServiceDep, response: Response, token: CurrentRefreshTokenDep) -> dict:
    
    await auth_service.logout(token)
    
    security.unset_access_cookies(response)
    security.unset_refresh_cookies(response)
    
    return {'message': 'Вы вышли из аккаунта'}