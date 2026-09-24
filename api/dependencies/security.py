from typing import Annotated
from uuid import UUID
from authx import TokenPayload
from fastapi import Depends, HTTPException, Request
from .repositories import RefreshTokenRepositoryDep
from models import RefreshToken
from core import security, settings



AccessTokenPayloadDep = Annotated[TokenPayload, Depends(security.access_token_required)]
RefreshTokenPayloadDep = Annotated[TokenPayload, Depends(security.refresh_token_required)]


async def require_admin(payload: AccessTokenPayloadDep) -> TokenPayload:
    if not payload.is_admin:
        raise HTTPException(status_code=403, detail='Недостаточно прав')

    return payload



def get_user_id(payload: AccessTokenPayloadDep) -> UUID:
    try:
        user_id = UUID(payload.sub)
        return user_id
    except ValueError:
        raise HTTPException(status_code=401, detail='Неверный формат идентификатора')
    
UserIdDep = Annotated[UUID, Depends(get_user_id)]


async def get_current_refresh_token(request: Request, payload: RefreshTokenPayloadDep, refresh_repo: RefreshTokenRepositoryDep) -> RefreshToken:
    
    token = request.cookies.get(settings.jwt_refresh_cookie_name)
        
    if token is None:
        raise HTTPException(status_code=401, detail='Refresh токен отсутствует')
    
    try:
        user_id = UUID(payload.sub)
    except ValueError:
        raise HTTPException(status_code=401, detail='Неверный формат идентификатора')

    stored_token = await refresh_repo.get_by_token_and_user(token, user_id)
    
    if stored_token is None:
        raise HTTPException(status_code=401, detail='Refresh токен не найден')
    
    return stored_token

CurrentRefreshTokenDep = Annotated[RefreshToken, Depends(get_current_refresh_token)]