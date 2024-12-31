from fastapi import APIRouter, status, Depends
from typing import List
from sqlmodel import select
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from . import templates, SessionDependancy
from .models import Service
from .schemas import ServiceForm

service = APIRouter()

@service.get("/sales", response_class=HTMLResponse)
async def sales(request: Request):
    return templates.TemplateResponse("pages/sales.html", {"request": request})

@service.get("/clients", response_class=HTMLResponse)
async def clients(request: Request):
    return templates.TemplateResponse("pages/clients.html", {"request": request})

@service.get("/services", response_model=List[Service])
async def services(request: Request, session: SessionDependancy):
    statement = select(Service)
    services = session.exec(statement).all()
    return templates.TemplateResponse("pages/services.html", {"request": request, "services": services})

@service.post("/add-new-service", response_class=HTMLResponse, response_model=Service, status_code=status.HTTP_200_OK)
async def add_new_service(request: Request, session: SessionDependancy, form: ServiceForm = Depends(ServiceForm.as_form)):
    data = {
        "name": form.name,
        "cost": form.cost,
        "commission": form.commission,
        "discount": form.discount,
        "status": form.status,
        "availability": form.availability
    }
    created_item = Service(**data)
    session.add(created_item)
    session.commit()
    return created_item