from typing import Annotated
from fastapi import Depends

from repositories import UserRepository, RefreshTokenRepository, ProductRepository
from services import AuthService, UserService, ProductService

from .repositories import get_user_repo, get_refresh_repo, get_product_repo  


def get_auth_service(
    user_repo: Annotated[UserRepository, Depends(get_user_repo)],
    refresh_repo: Annotated[RefreshTokenRepository, Depends(get_refresh_repo)],
) -> AuthService:
    return AuthService(user_repo, refresh_repo)

AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]


def get_user_service(user_repo: Annotated[UserRepository, Depends(get_user_repo)]) -> UserService:
    return UserService(user_repo)

UserServiceDep = Annotated[UserService, Depends(get_user_service)]


def get_product_service(product_repo: Annotated[ProductRepository, Depends(get_product_repo)]) -> ProductService:
    return ProductService(product_repo)

ProductServiceDep = Annotated[ProductService, Depends(get_product_service)]