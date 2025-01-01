from fastapi import APIRouter, Depends, status
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from . import templates, SessionDependancy
from .schemas import StaffForm
from .models import Staff

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

@maintenance.post("/add-new-staff", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def add_new_staff(request: Request, session: SessionDependancy, form: StaffForm = Depends(StaffForm.as_form)):
    data = {
        "name": form.name,
        "role": form.role,
        "department": form.department,
        "contact": form.contact,
        "commission": form.commission,
        "salary": form.salary,
        "status": form.status
    }
    created_staff= Staff(**data)
    session.add(created_staff)
    session.commit()
    return created_staff