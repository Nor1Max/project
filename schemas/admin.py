from pydantic import BaseModel


    
class UpdateUserAdminSchema(BaseModel):
    
    first_name: str| None = None
    last_name: str | None = None
    age: int | None = None
    email: str | None = None
    phone: int | None = None
    
