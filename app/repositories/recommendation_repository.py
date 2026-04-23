from app.models.recommendation_log import RecommendationLog

def create_log(db, user_id, product_id, action_type):
    log = RecommendationLog(
        user_id=user_id,
        product_id=product_id,
        action_type=action_type
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log