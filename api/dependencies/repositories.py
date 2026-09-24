from typing import Annotated
from fastapi import Depends
from repositories import UserRepository, RefreshTokenRepository, ProductRepository, CartRepository

from .session import SessionDep     


def get_user_repo(session: SessionDep) -> UserRepository:
    return UserRepository(session)

UserRepositoryDep = Annotated[UserRepository, Depends(get_user_repo)]


def get_refresh_repo(session: SessionDep) -> RefreshTokenRepository:
    return RefreshTokenRepository(session)

RefreshTokenRepositoryDep = Annotated[RefreshTokenRepository, Depends(get_refresh_repo)]


def get_product_repo(session: SessionDep) -> ProductRepository:
    return ProductRepository(session)

ProductRepositoryDep = Annotated[ProductRepository, Depends(get_product_repo)]


def get_cart_repo(session: SessionDep) -> CartRepository:
    return CartRepository(session)

CartRepositoryDep = Annotated[CartRepository, Depends(get_cart_repo)]