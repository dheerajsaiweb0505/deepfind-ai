from pydantic import BaseModel


class SearchRequest(BaseModel):
    query: str


class SearchResult(BaseModel):
    title: str
    url: str
    snippet: str


class SearchResponse(BaseModel):
    results: list[SearchResult]