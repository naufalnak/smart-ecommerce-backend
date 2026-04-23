from sqlalchemy.orm import Session
from app.repositories.cart_repository import (
    get_cart_item,
    create_cart_item,
    update_cart_item,
    delete_cart_item,
    get_user_cart
)

def add_to_cart(db: Session, user_id: int, product_id: int, quantity: int):
    item = get_cart_item(db, user_id, product_id)

    if item:
        # jika sudah ada → tambah quantity
        item.quantity += quantity
        return update_cart_item(db, item, item.quantity)

    return create_cart_item(db, user_id, product_id, quantity)


def update_cart(db: Session, user_id: int, product_id: int, quantity: int):
    item = get_cart_item(db, user_id, product_id)

    if not item:
        raise Exception("Item not found")

    if quantity <= 0:
        delete_cart_item(db, item)
        return None

    return update_cart_item(db, item, quantity)


def remove_from_cart(db: Session, user_id: int, product_id: int):
    item = get_cart_item(db, user_id, product_id)

    if not item:
        raise Exception("Item not found")

    delete_cart_item(db, item)


def get_cart(db: Session, user_id: int):
    return get_user_cart(db, user_id)