from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.requests import Request
from . import templates, SessionDependancy
from .schemas import StaffForm
from .models import Staff
from typing import List
from sqlmodel import select

maintenance = APIRouter()

@maintenance.get("/settings", response_class=HTMLResponse)
async def settings(request: Request):
    return templates.TemplateResponse("pages/settings.html", {"request": request})


@maintenance.get("/staff", response_class=HTMLResponse, response_model=List[Staff])
async def staff(request: Request, session: SessionDependancy):
    statement = select(Staff)
    result = session.exec(statement).all()
    return templates.TemplateResponse("pages/staff.html", {"request": request, "staffs": result})


@maintenance.post("/add-new-staff", response_class=HTMLResponse, status_code=status.HTTP_201_CREATED)
async def add_new_staff(request: Request, session: SessionDependancy, form: StaffForm = Depends(StaffForm.as_form)):
    created_staff= Staff(**form.dict())
    session.add(created_staff)
    session.commit()
    session.refresh(created_staff)
    redirect_url = request.url_for('staff')
    return RedirectResponse(redirect_url, status_code=status.HTTP_201_CREATED)


@maintenance.get("/details/{staff_id}")
async def staff_details(request: Request, staff_id: int, session: SessionDependancy):
    staff = session.get(Staff, staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff Not Found")
    return templates.TemplateResponse("pages/details.html", {"request": request, "staff": staff})


@maintenance.get("/delete-staff/{staff_id}", response_class=HTMLResponse)
async def delete_staff(request: Request, staff_id: int, session: SessionDependancy):
    pass


@maintenance.put("/update-staff/{staff_id}")
async def update_staff(request: Request, staff_id: int, session: SessionDependancy):
    pass