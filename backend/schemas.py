from pydantic import BaseModel
from fastapi import Form

class UserAdminForm(BaseModel):
    username: str
    password: str

    @classmethod
    def as_form(
        cls,
        username: str = Form(...),
        password: str = Form(...)
    ) -> "UserAdminForm":
        return cls(**locals())

class ServiceForm(BaseModel):
    name: str
    cost: int
    commission: int
    discount: int
    status: str
    availability: str

    @classmethod
    def as_form(
        cls,
        name: str = Form(...),
        cost: int = Form(...),
        commission: int = Form(...),
        discount: int = Form(...),
        status: str = Form(...),
        availability: str = Form(...)
    ) -> "ServiceForm":
        return cls(**locals())
    
class StaffForm(BaseModel):
    name: str
    staff_id: int
    email: str
    gender: str
    role: str
    department: str
    contact: str
    commission: int
    salary: int
    status: str

    @classmethod
    def as_form(
        cls,
        name: str = Form(...),
        staff_id: int = Form(...),
        email: str = Form(...),
        gender: str = Form(...),
        role: str = Form(...),
        department: str = Form(...),
        contact: str = Form(...),
        commission: int = Form(...),
        salary: int = Form(...),
        status: str = Form(...)
    ) -> "StaffForm":
        return cls(**locals())