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

class Transaction(BaseModel, table=True):
    vehicle: str = Field(nullable=False)

class Report(BaseModel, table=True):
    report_type: str = Field(nullable=False)

class Service(BaseModel, table=True):
    name: str = Field(nullable=True)
    cost: int = Field(nullable=True)
    commission: int = Field(nullable=True)
    discount: int = Field(nullable=True)
    status: str = Field(nullable=True)
    availability: str = Field(nullable=True)