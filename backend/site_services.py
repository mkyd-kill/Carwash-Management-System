from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from . import templates, SessionDependancy, crudDependancy
from typing import List
from .models import Service

service = APIRouter()

@service.get("/sales", response_class=HTMLResponse)
async def sales(request: Request):
    return templates.TemplateResponse("pages/sales.html", {"request": request})

@service.get("/clients", response_class=HTMLResponse)
async def clients(request: Request):
    return templates.TemplateResponse("pages/clients.html", {"request": request})

@service.get("/services", response_class=HTMLResponse)
async def services(request: Request):
    return templates.TemplateResponse("pages/services.html", {"request": request})

@service.post("/add-new-service", response_class=HTMLResponse, response_model=Service, status_code=status.HTTP_200_OK)
async def add_new_service(request: Request, session: SessionDependancy, cqrs: crudDependancy):
    data = {
        "name": request.get["name"],
        "cost": request.get["cost"],
        "commission": request.get["commission"],
        "discount": request.get["discount"],
        "status": request.get["status"],
        "availability": request.get["availability"]
    }
    created_item = await cqrs.create_obj(Service, session, data)
    return created_item