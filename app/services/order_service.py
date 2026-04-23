from sqlalchemy.orm import Session
from app.repositories.order_repository import create_order, create_order_item
from app.repositories.cart_repository import get_user_cart
from app.models.user import User
from app.workers.tasks import send_order_confirmation

def checkout(db: Session, user_id: int):
    cart_items = get_user_cart(db, user_id)

    if not cart_items:
        raise Exception("Cart is empty")

    # ambil user berdasarkan user_id
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise Exception("User not found")

    total_price = 0

    for item in cart_items:
        total_price += item.product.price * item.quantity

    try:
        order = create_order(
            db,
            user_id,
            total_price
        )

        for item in cart_items:
            create_order_item(
                db,
                order.id,
                item.product_id,
                item.quantity,
                item.product.price
            )

        for item in cart_items:
            db.delete(item)

        db.commit()

        # trigger async email
        send_order_confirmation.delay(
            user.email,
            order.id
        )

        return order

    except Exception as e:
        db.rollback()
        raise e
    
    