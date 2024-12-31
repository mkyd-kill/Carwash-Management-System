from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from . import templates
from .schemas import UserAdmin

auth = APIRouter()

@auth.get("/")
def get_login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@auth.post("/login", response_class=HTMLResponse)
def post_login_form(request: Request, form: UserAdmin = Depends(UserAdmin.as_form)):
    print(form)
    return templates.TemplateResponse("login.html", {"request": request})

@auth.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    data = {
            "request": request,
            "title": "Dashboard"
    }
    return templates.TemplateResponse("pages/dashboard.html", data)

@auth.post("/logout", response_class=HTMLResponse)
def logout(request: Request):
    pass