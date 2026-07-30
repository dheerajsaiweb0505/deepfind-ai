from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password


class UserRepository:

    @staticmethod
    def get_by_email(db: Session, email: str):
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    @staticmethod
    def get_by_username(db: Session, username: str):
        return (
            db.query(User)
            .filter(User.username == username)
            .first()
        )

    @staticmethod
    def create_user(
        db: Session,
        user: UserCreate
    ):
        db_user = User(
            username=user.username,
            email=user.email,
            hashed_password=hash_password(user.password)
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

from app.models.search_history import SearchHistory


class SearchRepository:

    @staticmethod
    def create(
        db,
        query,
        user_id
    ):

        search = SearchHistory(
            query=query,
            user_id=user_id
        )

        db.add(search)

        db.commit()

        db.refresh(search)

        return search

    @staticmethod
    def get_recent(
        db,
        user_id,
        limit=10
    ):

        return (
            db.query(SearchHistory)
            .filter(
                SearchHistory.user_id == user_id
            )
            .order_by(
                SearchHistory.created_at.desc()
            )
            .limit(limit)
            .all()
        )