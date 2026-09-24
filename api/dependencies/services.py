from typing import Annotated
from fastapi import Depends

from services import AuthService, UserService, ProductService, CartService
from .repositories import UserRepositoryDep, RefreshTokenRepositoryDep, ProductRepositoryDep, CartRepositoryDep


def get_auth_service(
    user_repo: UserRepositoryDep,
    refresh_repo: RefreshTokenRepositoryDep,
) -> AuthService:
    return AuthService(user_repo, refresh_repo)

AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]


def get_user_service(user_repo: UserRepositoryDep) -> UserService:
    return UserService(user_repo)

UserServiceDep = Annotated[UserService, Depends(get_user_service)]


def get_product_service(product_repo: ProductRepositoryDep) -> ProductService:
    return ProductService(product_repo)

ProductServiceDep = Annotated[ProductService, Depends(get_product_service)]


def get_cart_service(cart_repo: CartRepositoryDep, product_repo: ProductRepositoryDep) -> CartService:
    return CartService(cart_repo, product_repo)

CartServiceDep = Annotated[CartService, Depends(get_cart_service)]