from fastapi import APIRouter, Depends, status
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from . import templates, SessionDependancy
from .schemas import UserAdminForm, Token
from .models import Admin
from dotenv import load_dotenv
import os

load_dotenv()

auth = APIRouter()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/token")

@auth.get("/")
async def get_login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@auth.post("/", response_class=HTMLResponse)
async def post_login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@auth.post("/register-new-admin", response_class=HTMLResponse, status_code=status.HTTP_201_CREATED)
async def post_register_form(request: Request, session: SessionDependancy, admin_form: UserAdminForm = Depends(UserAdminForm.as_form)):
    user_input_form = Admin(**admin_form.dict())
    create_admin_model = Admin(
        username=user_input_form.username,
        password=bcrypt_context.hash(user_input_form.password)
    )
    session.add(create_admin_model)
    session.commit()
    return templates.TemplateResponse("pages/dashboard.html", {"request": request})

@auth.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("pages/dashboard.html", {"request": request})

@auth.post("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    pass