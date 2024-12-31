from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from . import templates

maintenance = APIRouter()

@maintenance.get("/branch", response_class=HTMLResponse)
async def branch(request: Request):
    return templates.TemplateResponse("pages/branch.html", {"request": request})

@maintenance.get("/settings", response_class=HTMLResponse)
async def settings(request: Request):
    return templates.TemplateResponse("pages/settings.html", {"request": request})

@maintenance.get("/staff", response_class=HTMLResponse)
async def staff(request: Request):
    return templates.TemplateResponse("pages/staff.html", {"request": request})