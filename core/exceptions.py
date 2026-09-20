class AppError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)
        
class NotFoundError(AppError):
    def __init__(self, entity: str):
        super().__init__(f'{entity} не найден')
        
class AlreadyExistsError(AppError):
    def __init__(self, entity: str):
        super().__init__(f'{entity} уже существует')


class InvalidCredentialsError(AppError):
    def __init__(self):
        super().__init__('Неверный email или пароль')
        
class InvalidTokenError(AppError):
    def __init__(self):
            super().__init__('Некорректный токен')