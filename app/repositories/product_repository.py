from sqlalchemy.orm import Session
from app.models.product import Product

def create_product(db: Session, data):
    product = Product(**data)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_products(db: Session, skip: int = 0, limit: int = 10, category_id: int = None):
    query = db.query(Product)

    if category_id:
        query = query.filter(Product.category_id == category_id)

    return query.offset(skip).limit(limit).all()