from fastapi import APIRouter
from api.dependencies import CartServiceDep, AccessTokenPayloadDep
from schemas import CartOperationSchema, CartResponseSchema
from models import Cart


router = APIRouter(tags=['Cart'])


@router.get('/user_cart', response_model=list[CartResponseSchema])
async def get_user_cart(cart_service: CartServiceDep, payload: AccessTokenPayloadDep) -> list[CartResponseSchema]:
    return await cart_service.get_user_cart(payload.sub)


@router.post('/increase_product', response_model=CartResponseSchema)
async def increase_product(cart_service: CartServiceDep, payload: AccessTokenPayloadDep, data: CartOperationSchema) -> Cart:
    return await cart_service.increase_product(payload.sub, data)


@router.post('/decrease_product', response_model=CartResponseSchema | None)
async def decrease_product(cart_service: CartServiceDep, payload: AccessTokenPayloadDep, data: CartOperationSchema) -> Cart | None:
    return await cart_service.decrease_product(payload.sub, data)
