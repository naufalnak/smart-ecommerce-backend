from sqlalchemy.orm import Session
from app.repositories.user_repository import get_user_by_email, create_user
from app.core.security import hash_password, verify_password, create_access_token

def register_user(db: Session, email: str, password: str):
    existing = get_user_by_email(db, email)
    if existing:
        raise Exception("Email already registered")

    hashed = hash_password(password)
    return create_user(db, email, hashed)


def login_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)

    if not user or not verify_password(password, user.password):
        raise Exception("Invalid credentials")

    token = create_access_token({
        "sub": user.email,
        "user_id": user.id
    })

    return token