from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Numeric
from core import BaseUUID
from decimal import Decimal


class Product(BaseUUID):
    __tablename__ = 'products'
    
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str | None] 
    weight: Mapped[int]
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    
    carts: Mapped[list['Cart']] = relationship(back_populates='product')
    