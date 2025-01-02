from pydantic import BaseModel
from fastapi import Form

class UserAdmin(BaseModel):
    username: str
    password: str

    @classmethod
    def as_form(cls, username: str = Form(...), password: str = Form(...)):
        return cls(
            username=username,
            password=password
        )

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
    ):
        return cls(
            name=name,
            cost=cost,
            commission=commission,
            discount=discount,
            status=status,
            availability=availability
        )
    
class StaffForm(BaseModel):
    name: str
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
        gender: str = Form(...),
        role: str = Form(...),
        department: str = Form(...),
        contact: str = Form(...),
        commission: int = Form(...),
        salary: int = Form(...),
        status: str = Form(...)
    ):
        return cls(
            name=name,
            gender=gender,
            role=role,
            department=department,
            contact=contact,
            commission=commission,
            salary=salary,
            status=status
        )