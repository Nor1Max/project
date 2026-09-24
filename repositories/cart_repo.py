from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from models import Cart



class CartRepository:
    
    def __init__(self, session: AsyncSession):
        self.session = session
        
    
    async def get_user_cart(self, user_id: UUID) -> list[Cart]:
        stmt = (
            select(Cart)
            .where(
                Cart.user_id == user_id
            )
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    
    async def get_product_by_id(self, user_id: UUID, product_id: UUID) -> Cart | None:
        stmt = (
            select(Cart)
            .where(
                Cart.user_id == user_id,
                Cart.product_id == product_id
            )
        )
        result = await self.session.execute(stmt)
        
        return result.scalar_one_or_none()
    
    
    async def create(self, data: dict) -> Cart:
            
        product = Cart(**data)
        
        self.session.add(product)
        
        await self.session.commit()
        await self.session.refresh(product)
    
        return product
        
    
    
    async def increase_quantity(self, product: Cart) -> Cart:
        
        product.quantity += 1
            
        await self.session.commit()
        await self.session.refresh(product)
        
        return product
    
    
    async def decrease_quantity(self, product: Cart) -> Cart:

        product.quantity -= 1           
        
        await self.session.commit()
        await self.session.refresh(product)
        
        return product
    
    
    async def delete(self, product: Cart) -> None:
        await self.session.delete(product)
        await self.session.commit()
        
    