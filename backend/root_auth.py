from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
# # from jose import JWTError, jwt
# from passlib.context import CryptContext
from . import templates
from .schemas import UserAdminForm
from typing import Annotated
from dotenv import load_dotenv
import os

load_dotenv()

auth = APIRouter()

form_dependancy = Annotated[UserAdminForm, Depends(UserAdminForm.as_form)]

@auth.get("/")
async def get_login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@auth.post("/", response_class=HTMLResponse)
async def post_login_form(request: Request, form: form_dependancy):
    return templates.TemplateResponse("login.html", {"request": request})

@auth.post("/", response_class=HTMLResponse)
async def post_register_form(request: Request, form: form_dependancy):
    return templates.TemplateResponse("login.html", {"request": request})

@auth.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("pages/dashboard.html", {"request": request})

@auth.post("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    pass