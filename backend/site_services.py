from fastapi import APIRouter, status, Depends
from typing import List
from sqlmodel import select
from fastapi.responses import HTMLResponse, RedirectResponse
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

@service.post("/add-new-service", response_class=HTMLResponse, status_code=status.HTTP_201_CREATED)
async def add_new_service(request: Request, session: SessionDependancy, form: ServiceForm = Depends(ServiceForm.as_form)):
    created_item = Service(**form.dict())
    session.add(created_item)
    session.commit()
    session.refresh(created_item)
    redirect_url = request.url_for('services')
    return RedirectResponse(redirect_url, status_code=status.HTTP_201_CREATED)