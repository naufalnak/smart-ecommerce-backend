from sqlalchemy.orm import Session
from app.repositories.product_repository import create_product, get_products

def create_new_product(db: Session, data):
    return create_product(db, data)

def list_products(db: Session, skip=0, limit=10, category_id=None):
    return get_products(db, skip, limit, category_id)