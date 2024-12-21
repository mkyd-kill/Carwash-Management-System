from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from . import templates

auth = APIRouter()

@auth.get("/")
async def root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@auth.post("/login")
async def login():
    pass

@auth.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    data = {
            "request": request,
            "title": "Dashboard"
    }
    return templates.TemplateResponse("pages/dashboard.html", data)

@auth.post("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    pass