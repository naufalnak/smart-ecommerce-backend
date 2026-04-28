from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.order_service import checkout
from app.db.database import get_db
from app.core.security import get_current_user

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post("/checkout")
def checkout_order(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    order = checkout(
        db,
        user["user_id"]
    )

    return {
        "success": True,
        "message": "Checkout success",
        "data": {
            "order_id": order.id,
            "total_price": order.total_price
        }
    }