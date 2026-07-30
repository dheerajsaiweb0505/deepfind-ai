from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserLogin
from app.core.security import (
    verify_password,
    create_access_token
)


class AuthService:

    @staticmethod
    def register(
        db: Session,
        user: UserCreate
    ):
        if UserRepository.get_by_email(db, user.email):
            raise ValueError("Email already registered")

        if UserRepository.get_by_username(db, user.username):
            raise ValueError("Username already exists")

        return UserRepository.create_user(db, user)

    @staticmethod
    def login(
        db: Session,
        credentials: UserLogin
    ):
        user = UserRepository.get_by_email(
            db,
            credentials.email
        )

        if not user:
            raise ValueError("Invalid email or password")

        if not verify_password(
            credentials.password,
            user.hashed_password
        ):
            raise ValueError("Invalid email or password")

        token = create_access_token(
            {
                "sub": user.email
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }