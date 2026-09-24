from uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, CheckConstraint
from core import Base, created_at, updated_at


class Cart(Base):
    __tablename__ = 'carts'
    __table_args__ = (
        CheckConstraint('quantity >= 1', name='cart_quantity_positive'),
    )
    
    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    product_id: Mapped[UUID] = mapped_column(ForeignKey('products.id', ondelete='CASCADE'), primary_key=True)
    quantity: Mapped[int] = mapped_column(default=1)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    
    product: Mapped['Product'] = relationship(back_populates='carts', lazy='selectin')
    user: Mapped['User'] = relationship(back_populates='carts', lazy='selectin')