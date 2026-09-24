from fastapi import APIRouter
from .auth import router as auth_router
from .profile import router as profile_router
from .product import router as product_router
from .admin import router as admin_router
from .cart import router as cart_router

main_router = APIRouter()

main_router.include_router(auth_router, prefix='/auth')
main_router.include_router(profile_router, prefix='/profile')
main_router.include_router(product_router, prefix='/product')
main_router.include_router(admin_router, prefix='/admin')
main_router.include_router(cart_router, prefix='/cart')
