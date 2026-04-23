from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.cart import AddToCart, UpdateCart
from app.services.cart_service import add_to_cart, update_cart, remove_from_cart, get_cart
from app.db.database import get_db
from app.core.security import get_current_user

router = APIRouter(prefix="/cart", tags=["Cart"])


@router.post("/")
def add_item(
    data: AddToCart,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return add_to_cart(db, user["user_id"], data.product_id, data.quantity)


@router.put("/{product_id}")
def update_item(
    product_id: int,
    data: UpdateCart,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    try:
        return update_cart(db, user["user_id"], product_id, data.quantity)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{product_id}")
def delete_item(
    product_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    try:
        remove_from_cart(db, user["user_id"], product_id)
        return {"message": "Item removed"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
def get_items(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return get_cart(db, user["user_id"])