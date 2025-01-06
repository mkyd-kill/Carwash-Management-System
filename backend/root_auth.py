from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from . import templates
from .schemas import UserAdminForm

auth = APIRouter()

@auth.get("/")
async def get_login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@auth.post("/login", response_class=HTMLResponse)
async def post_login_form(request: Request, form: UserAdminForm = Depends(UserAdminForm.as_form)):
    print(form)
    return templates.TemplateResponse("login.html", {"request": request})

@auth.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("pages/dashboard.html", {"request": request})

@auth.post("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    pass