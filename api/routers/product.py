from fastapi import Depends, APIRouter
from uuid import UUID
from api.dependencies import ProductServiceDep, require_admin
from schemas import CreateProductSchema, UpdateProductSchema, ProductResponseSchema


router = APIRouter(tags=['Product'])


@router.get('/all', response_model=list[ProductResponseSchema])
async def get_product_all(product_service: ProductServiceDep) -> list[ProductResponseSchema]:
    
    return await product_service.get_product_all()


@router.post('/create', dependencies=[Depends(require_admin)], response_model=ProductResponseSchema)
async def create_product(product_service: ProductServiceDep, data: CreateProductSchema) -> ProductResponseSchema: 
    
    return await product_service.create_product(data)


@router.get('/{product_id}', response_model=ProductResponseSchema)
async def get_product_by_id(product_service: ProductServiceDep, product_id: UUID) -> ProductResponseSchema:
    
    return await product_service.get_product_by_id(product_id)


@router.patch('/{product_id}', dependencies=[Depends(require_admin)], response_model=ProductResponseSchema)
async def update_product(product_service: ProductServiceDep, product_id: UUID, data: UpdateProductSchema) -> ProductResponseSchema:
    
    return await product_service.update_product(product_id, data)


@router.delete('/{product_id}', dependencies=[Depends(require_admin)])
async def delete_product(product_service: ProductServiceDep, product_id: UUID) -> dict:
    
    await product_service.delete_product(product_id)
    
    return {'message': 'Product удален из системы'}
    