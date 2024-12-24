from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from . import templates

service = APIRouter()

@service.get("/sales", response_class=HTMLResponse)
async def sales(request: Request):
    data = {
            "request": request,
            "title": "Sales"
    }
    return templates.TemplateResponse("pages/sales.html", data)

@service.get("/clients", response_class=HTMLResponse)
async def clients(request: Request):
    data = {
            "request": request,
            "title": "Clients"
    }
    return templates.TemplateResponse("pages/clients.html", data)

@service.get("/services", response_class=HTMLResponse)
async def services(request: Request):
    data = {
            "request": request,
            "title": "Services"
    }
    return templates.TemplateResponse("pages/services.html", data)

@service.post("/add-new-service", response_class=HTMLResponse)
async def add_new_service(request: Request):
    return "Url working okay"