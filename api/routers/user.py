from fastapi import APIRouter

from api.dependencies import AccessTokenPayloadDep


router = APIRouter(tags=['User'])


@router.get('/me')
async def get_me(payload: AccessTokenPayloadDep) -> dict:
    return {'id': payload.sub, 'is_admin': payload.is_admin}
    
