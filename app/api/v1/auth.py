from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserLogin,
)
from app.services.auth_service import AuthService

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


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    try:

        credentials = UserLogin(
            email=form_data.username,
            password=form_data.password,
        )

        token = AuthService.login(db, credentials)

        response = JSONResponse(
            content={
                "message": "Login successful"
            }
        )

        response.set_cookie(
            key="access_token",
            value=token["access_token"],
            httponly=True,
            samesite="lax",
            secure=False,      # True when using HTTPS
            max_age=3600
        )

        return response

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )


@router.post("/logout")
def logout():

    response = JSONResponse(
        content={
            "message": "Logged out successfully"
        }
    )

    response.delete_cookie("access_token")

    return response