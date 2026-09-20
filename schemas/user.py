from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class UserResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: UUID
    first_name: str
    last_name: str 
    age: int | None 
    email: str 
    phone: int | None 
    is_admin: bool
    created_at: datetime
    