from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session


from app.db.database import get_db
from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserLogin,
    Token,
)
from app.services.auth_service import AuthService
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    try:
        return AuthService.register(db, user)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post("/login", response_model=Token)
def login(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    try:
        credentials = UserLogin(
            email=form_data.username,
            password=form_data.password,
        )

        token = AuthService.login(db, credentials)

        response.set_cookie(
            key="access_token",
            value=token["access_token"],   # <-- FIX
            httponly=True,
            samesite="lax",
            secure=False,
            max_age=86400,
        )

        return token

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )