from uuid import UUID
from pydantic import BaseModel, ConfigDict
from schemas import ProductResponseSchema


class CartOperationSchema(BaseModel):
    product_id: UUID
    

    
class CartResponseSchema(BaseModel):
    
    product_id: UUID
    quantity: int
    product: ProductResponseSchema
    
    model_config = ConfigDict(from_attributes=True)