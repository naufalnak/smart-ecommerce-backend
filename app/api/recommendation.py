from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.recommendation_service import get_recommendations
from app.db.database import get_db
from app.core.security import get_current_user

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)

@router.get("/")
def recommend(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    products = get_recommendations(
        db,
        user["user_id"]
    )

    return [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price
        }
        for p in products
    ]