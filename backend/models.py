from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

class BaseModel(SQLModel):
    id: Optional[int] = Field(primary_key=True)
    date_created: Optional[datetime] = Field(default_factory=lambda: datetime.now())

class AdminModel(BaseModel, table=True):
    username: str = Field(nullable=False)
    password: str = Field(nullable=False)

class Clients(BaseModel, table=True):
    vehicle: str = Field(nullable=False)

class Staff(BaseModel, table=True):
    name: str = Field(nullable=False)
    role: str = Field(nullable=False)
    department: str = Field(nullable=False)
    contact: str = Field(nullable=False)
    commission: int = Field(nullable=False)
    salary: int = Field(nullable=False)
    status: str = Field(nullable=False)

class Transaction(BaseModel, table=True):
    vehicle: str = Field(nullable=False)

class Report(BaseModel, table=True):
    report_type: str = Field(nullable=False)

class Service(BaseModel, table=True):
    name: str = Field(nullable=False)
    cost: int = Field(nullable=False)
    commission: int = Field(nullable=False)
    discount: int = Field(nullable=False)
    status: str = Field(nullable=False)
    availability: str = Field(nullable=False)