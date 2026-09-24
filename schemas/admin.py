from datetime import datetime
from schemas import UserResponseSchema


    
class AdminResponseSchema(UserResponseSchema):
    
    created_at: datetime
    updated_at: datetime

