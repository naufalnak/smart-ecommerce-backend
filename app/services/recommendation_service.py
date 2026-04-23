from sqlalchemy.orm import Session
from collections import Counter
from app.models.recommendation_log import RecommendationLog
from app.models.product import Product

def get_recommendations(db: Session, user_id: int):
    logs = db.query(RecommendationLog).filter(
        RecommendationLog.user_id == user_id
    ).all()

    if not logs:
        return db.query(Product).limit(5).all()

    product_ids = [log.product_id for log in logs]

    products = db.query(Product).filter(
        Product.id.in_(product_ids)
    ).all()

    category_ids = [p.category_id for p in products]

    most_common_category = Counter(category_ids).most_common(1)

    if not most_common_category:
        return []

    category_id = most_common_category[0][0]

    recommendations = db.query(Product).filter(
        Product.category_id == category_id,
        Product.id.notin_(product_ids)
    ).limit(5).all()

    return recommendations