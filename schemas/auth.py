from uuid import UUID
from pydantic import ConfigDict, EmailStr, BaseModel, Field


class CreateUserSchema(BaseModel):
    
    first_name: str = Field(min_length=2, max_length=50, default=None)
    last_name: str = Field(min_length=2, max_length=50, default=None)
    email: EmailStr
    password: str
    
    
class CreateUserResponseSchema(BaseModel):
    
    id: UUID
    first_name: str
    last_name: str
    email: EmailStr
    
    model_config = ConfigDict(from_attributes=True)
    
    
class LoginUserSchema(BaseModel):
    
    email: EmailStr
    password: str