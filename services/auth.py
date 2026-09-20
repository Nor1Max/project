from uuid import UUID
from authx import TokenPayload
from models import RefreshToken, User
from schemas import CreateUserSchema, LoginUserSchema
from core import password_hash, security
from repositories import UserRepository, RefreshTokenRepository
from core import AlreadyExistsError, InvalidCredentialsError, InvalidTokenError



class AuthService:
    
    def __init__(self, user_repo: UserRepository, refresh_repo: RefreshTokenRepository):
        self.user_repo = user_repo
        self.refresh_repo = refresh_repo
    
    
    async def register_user(self, data: CreateUserSchema) -> User:
        
        existing = await self.user_repo.get_by_email(data.email)
        
        if existing:
            raise AlreadyExistsError('User')

        hashed_password = password_hash.hash(data.password)
        
        user_data = {
            'first_name': data.first_name,
            'last_name': data.last_name,
            'email': data.email,
            'password': hashed_password,
            'is_admin': False
        }

        new_user = await self.user_repo.create(user_data)
        
        return new_user
        
        
    async def login_user(self, data: LoginUserSchema) -> tuple[str, str]:
        user = await self.user_repo.get_by_email(data.email)
        
        if not user or not password_hash.verify(data.password, user.password):
            raise InvalidCredentialsError()

        access_token = security.create_access_token(
            uid=str(user.id),
            data={
                'is_admin': user.is_admin
            }
        )
        refresh_token = security.create_refresh_token(uid=str(user.id))
        
        await self.refresh_repo.create(refresh_token, user.id)
        
        return access_token, refresh_token
    
    
    async def refresh_access_token(self, payload: TokenPayload) -> str:
        
        try:
            user_id = UUID(payload.sub)
        except ValueError as e:
            raise InvalidTokenError() from e
        
        user = await self.user_repo.get_by_id(user_id)
        
        if not user:
            raise InvalidTokenError()
        
        new_access_token = security.create_access_token(
            uid=str(user.id),
            data={
                'is_admin': user.is_admin
            }
        )
        
        return new_access_token
    
    
    async def logout(self, refresh_token: RefreshToken) -> None:
        await self.refresh_repo.delete(refresh_token)
