from fastapi import APIRouter

from app.schemas.search import (
    SearchRequest,
    SearchResponse
)

from app.services.search_service import SearchService

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.post(
    "",
    response_model=SearchResponse
)
def search(
    request: SearchRequest
):

    results = SearchService.search(
        request.query
    )

    return {
        "results": results
    }