from fastapi import APIRouter, Depends, status, HTTPException
from typing import Annotated
from sqlmodel import select
from fastapi.responses import HTMLResponse, RedirectResponse
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


@auth.post("/register-new-admin", response_class=HTMLResponse, status_code=status.HTTP_201_CREATED)
async def post_register_form(request: Request, session: SessionDependancy, admin_form: UserAdminForm = Depends(UserAdminForm.as_form)):
    user_input_form = Admin(**admin_form.dict())
    # check if the username is already in the database
    statement = select(Admin).filter(Admin.username == user_input_form.username)
    database_user = session.exec(statement).first()
    if database_user:
        raise HTTPException(status=status.HTTP_302_FOUND, detail=f"{user_input_form.username} already exists. Try Another Username")
    create_admin_model = Admin(
        username=user_input_form.username,
        password=bcrypt_context.hash(user_input_form.password)
    )
    session.add(create_admin_model)
    session.commit()
    return RedirectResponse(url="/", status_code=status.HTTP_201_CREATED)


def authenticate_user(username: str, password: str, db):
    user = db.query(Admin).filter(Admin.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.password):
        return False
    return user

def create_access_token(username: str, user_id: int, expires_delta: timedelta | None):
    encode = {'sub': username, 'id': user_id}
    if expires_delta:
        expires = datetime.utcnow() + expires_delta
    else:
        expires = datetime.utcnow() + timedelta(60)
    encode.update({'exp': expires})
    return jwt.encode(encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("HASH_ALGORITHM"))


@auth.post("/token", response_model=Token)
async def login_for_access_token(request: Request, form_data: Annotated[OAuth2PasswordRequestForm, Depends(UserAdminForm.as_form)], db: SessionDependancy):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user")
    
    token = create_access_token(user.username, user.id, expires_delta=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

    return RedirectResponse(url="/dashboard", status_code=status.HTTP_200_OK, headers={'access_token': token, 'token_type': 'bearer'})


@auth.post("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    pass


@auth.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("pages/dashboard.html", {"request": request})