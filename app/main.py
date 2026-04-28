from fastapi import FastAPI, Depends, Request
import time

from app.core.security import get_current_user
from app.core.logger import logger
from app.core.exceptions import (
    AppException,
    app_exception_handler
)

from app.api import (
    auth,
    cart,
    product,
    category,
    order,
    recommendation
)

app = FastAPI(
    title="Smart E-Commerce API",
    version="1.0.0"
)

# Global exception handler
app.add_exception_handler(
    AppException,
    app_exception_handler
)

# Register routers
app.include_router(auth.router)
app.include_router(product.router)
app.include_router(category.router)
app.include_router(cart.router)
app.include_router(order.router)
app.include_router(recommendation.router)


@app.get("/")
def root():
    return {
        "message": "API is running 🚀"
    }


@app.get("/me")
def get_me(user=Depends(get_current_user)):
    return {
        "user": user
    }


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    logger.info(
        f"{request.method} {request.url.path} "
        f"completed in {process_time:.2f}s"
    )

    return response