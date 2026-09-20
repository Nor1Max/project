from fastapi import FastAPI
from core.security import security
from api.routers import main_router
from api.error_handlers import register_exception_handlers


app = FastAPI()

register_exception_handlers(app)

security.handle_errors(app)

app.include_router(main_router)






