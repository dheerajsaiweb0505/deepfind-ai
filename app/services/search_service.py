from app.schemas.search import SearchResult


class SearchService:

    @staticmethod
    def search(query: str):

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