from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from core import AppError, AlreadyExistsError, NotFoundError, InvalidCredentialsError, InvalidTokenError


async def not_found_handler(request: Request, exc: NotFoundError) -> JSONResponse:
    return JSONResponse(status_code=404, content={'detail': exc.message})

async def already_exists_handler(request: Request, exc: AlreadyExistsError) -> JSONResponse: 
    return JSONResponse(status_code=409, content={'detail': exc.message})

async def invalid_credentials_handler(request: Request, exc: InvalidCredentialsError) -> JSONResponse:
    return JSONResponse(status_code=401, content={'detail': exc.message})

async def invalid_token_handler(request: Request, exc: InvalidTokenError) -> JSONResponse:
    return JSONResponse(status_code=401, content={'detail': exc.message})

async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    return JSONResponse(status_code=500, content={'detail': exc.message})



def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(NotFoundError, not_found_handler)
    app.add_exception_handler(AlreadyExistsError, already_exists_handler)
    app.add_exception_handler(InvalidCredentialsError, invalid_credentials_handler)
    app.add_exception_handler(InvalidTokenError, invalid_token_handler)
    app.add_exception_handler(AppError, app_error_handler)