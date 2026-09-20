from sqlalchemy.orm import Mapped, mapped_column
from core import Base


class Product(Base):
    __tablename__ = 'products'
    
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str | None] 
    weight: Mapped[float]
    price: Mapped[float]
    