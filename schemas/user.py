from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field



class UpdateUserSchema(BaseModel):
    
    first_name: str| None = Field(min_length=2, max_length=50, default=None)
    last_name: str | None = Field(min_length=2, max_length=50, default=None)
    age: int | None = Field(ge=18, le=100, default=None)
    phone: int | None = Field(ge=70000000000, le=79999999999, default=None)




class UserResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: UUID
    first_name: str
    last_name: str 
    age: int | None
    email: str 
    phone: int | None 
    is_admin: bool
    
