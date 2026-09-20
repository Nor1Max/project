from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Product


class ProductRepository:
    
    def __init__(self, session: AsyncSession):
        self.session = session
    
    
    async def get_all(self) -> list[Product]:
    
        stmt = select(Product)
        result = await self.session.execute(stmt)
        
        return result.scalars().all()
    
    
    async def get_by_title(self, title: str) -> Product | None:

        stmt = (
                select(Product)
                .where(Product.title == title)   
            )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    
    async def create(self, product_data: dict) -> Product:
        
        new_product = Product(**product_data)
            
        self.session.add(new_product)
        await self.session.commit()
        await self.session.refresh(new_product)
        
        return new_product
    
    
    async def get_by_id(self, product_id: UUID) -> Product | None:
        return await self.session.get(Product, product_id)
    
    
    async def save(self, product: Product) -> Product:
        await self.session.commit()
        await self.session.refresh(product)
        
        return product
    
    
    async def delete(self, product: Product) -> None:
        await self.session.delete(product)
        await self.session.commit()