from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request, Depends
from app.core.config import settings

from app.core.security import get_current_user
from app.models.user import User

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)
from app.api.v1.router import api_router

app.include_router(api_router, prefix="/api/v1")


app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "request": request,
            "app_name": settings.APP_NAME,
        },
    )

@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
            "request": request
        }
    )

@app.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={
            "request": request
        }
    )


from fastapi import Depends
from app.core.security import get_current_user
from app.models.user import User

@app.get("/dashboard")
async def dashboard_page(
    request: Request,
    current_user: User = Depends(get_current_user),
):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "request": request,
            "user": current_user,
        },
    )