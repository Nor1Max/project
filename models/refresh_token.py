from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID
from core import BaseUUID


class RefreshToken(BaseUUID):
    __tablename__ = 'refresh_tokens'
    
    token: Mapped[str] = mapped_column(unique=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'))
    
    user: Mapped['User'] = relationship(back_populates='refresh_tokens')
    
    