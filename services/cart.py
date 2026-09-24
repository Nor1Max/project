from uuid import UUID
from repositories import CartRepository, ProductRepository
from schemas import CartOperationSchema
from core import NotFoundError
from models import Cart


class CartService:
    def __init__(self, cart_repo: CartRepository, product_repo: ProductRepository):
        self.cart_repo = cart_repo
        self.product_repo = product_repo
  
  
    async def get_user_cart(self, user_id: UUID) -> list[Cart]:
        return await self.cart_repo.get_user_cart(user_id)
    
    
    async def increase_product(self, user_id: UUID, data: CartOperationSchema) -> Cart:
        product = await self.cart_repo.get_product_by_id(user_id, data.product_id)

        if product is None:
            if await self.product_repo.get_by_id(data.product_id) is None:
                raise NotFoundError('Product')
            
            new_data = {
                "user_id": user_id, 
                "product_id": data.product_id, 
                "quantity": 1
            }
        
            return await self.cart_repo.create(new_data) 
        else:
            return await self.cart_repo.increase_quantity(product)
        

    async def decrease_product(self, user_id: UUID, data: CartOperationSchema) -> Cart | None:
        product = await self.cart_repo.get_product_by_id(user_id, data.product_id)
                        
        if product is None:
            raise NotFoundError('Product in Cart')
        
        if product.quantity > 1 :
            return await self.cart_repo.decrease_quantity(product) 
        else:
            await self.cart_repo.delete(product)
            return None
            
    

                
    
    

    
