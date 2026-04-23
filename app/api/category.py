from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.category import CategoryCreate
from app.repositories.category_repository import create_category, get_all_categories
from app.db.database import get_db
import json
from app.core.redis import redis_client

router = APIRouter(prefix="/categories", tags=["Category"])

@router.post("/")
def create(data: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, data.name)

@router.get("/")
def list_all(db: Session = Depends(get_db)):
    cache_key = "categories:all"

    cached_data = redis_client.get(cache_key)

    if cached_data:
        return {
            "source": "redis_cache",
            "data": json.loads(cached_data)
        }

    categories = get_all_categories(db)

    result = [
        {
            "id": c.id,
            "name": c.name
        }
        for c in categories
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