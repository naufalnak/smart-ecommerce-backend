from fastapi import FastAPI
from app.db.database import Base, engine
from app.models import user, product, category
from app.core.security import get_current_user
from fastapi import Depends
from app.api import auth, cart, product, category
from app.api import order
from app.api import recommendation

# ✅ app harus dibuat dulu
app = FastAPI(
    title="Smart E-Commerce API",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(product.router)
app.include_router(category.router)
app.include_router(cart.router)
app.include_router(order.router)
app.include_router(recommendation.router)


@app.get("/")
def root():
    return {"message": "API is running 🚀"}

@app.get("/me")
def get_me(user=Depends(get_current_user)):
    return {"user": user}