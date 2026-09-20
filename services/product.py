from uuid import UUID
from repositories import ProductRepository
from schemas import CreateProductSchema, UpdateProductSchema
from core import AlreadyExistsError, NotFoundError
from models import Product

class ProductService:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo
  
    
    async def get_product_all(self) -> list[Product]:
        
        return await self.product_repo.get_all()
    
    
    async def create_product(self, data: CreateProductSchema) -> Product:
        
        product = await self.product_repo.get_by_title(data.title)
        
        if product is not None:
            raise AlreadyExistsError('Product')
        
        product_data = data.model_dump()
        
        return await self.product_repo.create(product_data)
        
        
    async def get_product_by_id(self, product_id: UUID) -> Product:
        
        product = await self.product_repo.get_by_id(product_id)
        
        if product is None:
            raise NotFoundError('Product')
            
        return product
    

    
    async def update_product(self, product_id: UUID, data: UpdateProductSchema) -> Product:
        
        product = await self.product_repo.get_by_id(product_id)
        
        if product is None:
            raise NotFoundError('Product')
        
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(product, key, value)
        
        return await self.product_repo.save(product)
    
    
    async def delete_product(self, product_id: UUID) -> None:
        
        product = await self.product_repo.get_by_id(product_id)
        
        if product is None:
            raise NotFoundError('Product')
        
        await self.product_repo.delete(product)
    