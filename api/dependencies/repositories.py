from repositories import UserRepository, RefreshTokenRepository, ProductRepository

from .session import SessionDep     


def get_user_repo(session: SessionDep) -> UserRepository:
    return UserRepository(session)

def get_refresh_repo(session: SessionDep) -> RefreshTokenRepository:
    return RefreshTokenRepository(session)

def get_product_repo(session: SessionDep) -> ProductRepository:
    return ProductRepository(session)