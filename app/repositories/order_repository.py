from sqlalchemy.orm import Session
from app.models.order import Order
from app.models.order_item import OrderItem

def create_order(db: Session, user_id: int, total_price: float):
    order = Order(user_id=user_id, total_price=total_price)
    db.add(order)
    db.flush()  # penting untuk dapat order.id sebelum commit
    return order


def create_order_item(db: Session, order_id: int, product_id: int, quantity: int, price: float):
    item = OrderItem(
        order_id=order_id,
        product_id=product_id,
        quantity=quantity,
        price=price
    )
    db.add(item)