from pydantic import BaseModel


class CreateProductSchema(BaseModel):
    
    title: str
    description: str | None = None
    weight: float
    price: float
    
    
class UpdateProductSchema(BaseModel):
    
    title: str
    description: str | None = None
    weight: float 
    price: float 
    
    
class ProductResponseSchema(BaseModel):
    title: str
    description: str | None = None
    weight: float 
    price: float 
