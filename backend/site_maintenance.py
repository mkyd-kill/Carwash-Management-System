from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from . import templates

maintenance = APIRouter()

@maintenance.get("/branch", response_class=HTMLResponse)
async def branch(request: Request):
    data = {
            "request": request,
            "title": "Branch"
    }
    return templates.TemplateResponse("pages/branch.html", data)

@maintenance.get("/settings", response_class=HTMLResponse)
async def settings(request: Request):
    data = {
            "request": request,
            "title": "Settings"
    }
    return templates.TemplateResponse("pages/settings.html", data)

@maintenance.get("/staff", response_class=HTMLResponse)
async def staff(request: Request):
    data = {
            "request": request,
            "title": "Staff"
    }
    return templates.TemplateResponse("pages/staff.html", data)