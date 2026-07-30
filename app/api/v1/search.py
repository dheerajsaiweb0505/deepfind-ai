from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.core.security import get_current_user
from app.models.user import User

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
    request: SearchRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    results = SearchService.search(
        db=db,
        query=request.query,
        user=current_user,
    )

    return {
        "results": results
    }