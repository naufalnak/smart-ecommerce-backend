from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.logger import logger

class AppException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


async def app_exception_handler(
    request: Request,
    exc: AppException
):
    logger.error(exc.message)

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.message
        }
    )