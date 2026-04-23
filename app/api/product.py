from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate
from app.services.product_service import create_new_product, list_products
from app.db.database import get_db
import json
from app.core.redis import redis_client

router = APIRouter(prefix="/products", tags=["Product"])

@router.post("/")
def create(data: ProductCreate, db: Session = Depends(get_db)):
    return create_new_product(db, data.dict())

@router.get("/")
def get_all(
    skip: int = 0,
    limit: int = 10,
    category_id: int = None,
    db: Session = Depends(get_db)
):
    cache_key = f"products:{skip}:{limit}:{category_id}"

    cached_data = redis_client.get(cache_key)

    if cached_data:
        return {
            "source": "redis_cache",
            "data": json.loads(cached_data)
        }

    products = list_products(db, skip, limit, category_id)

    result = [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price
        }
        for p in products
    ]

    redis_client.setex(
        cache_key,
        300,
        json.dumps(result)
    )

    return {
        "source": "database",
        "data": result
    }