from sqlalchemy import func, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core import BaseUUID, created_at, updated_at




class User(BaseUUID):
    __tablename__ = 'users'
    
    first_name: Mapped[str]
    last_name: Mapped[str]
    age: Mapped[int | None]
    email: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[int | None] = mapped_column(BigInteger, unique=True)
    password: Mapped[str] 
    is_admin: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    
    
    refresh_tokens: Mapped[list['RefreshToken']] = relationship(back_populates='user')
    carts: Mapped[list['Cart']] = relationship(back_populates='user')
    