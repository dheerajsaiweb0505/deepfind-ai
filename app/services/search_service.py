from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.search_repository import SearchRepository
from app.schemas.search import SearchResult


class SearchService:

    @staticmethod
    def search(
        db: Session,
        query: str,
        user: User,
    ):

        # Save search history
        SearchRepository.save(
            db=db,
            query=query,
            user_id=user.id,
        )

        # Dummy results (replace with real search provider later)
        return [

            SearchResult(
                title="FastAPI Documentation",
                url="https://fastapi.tiangolo.com/",
                snippet="Modern, fast web framework for building APIs with Python."
            ),

            SearchResult(
                title="Python Official Documentation",
                url="https://docs.python.org/3/",
                snippet="Official Python documentation."
            ),

            SearchResult(
                title=f"Results for '{query}'",
                url="#",
                snippet="This is a dummy search result."
            )

        ]