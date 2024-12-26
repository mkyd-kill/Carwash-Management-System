from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from shortuuid import ShortUUID
from string import digits

class BaseModel(SQLModel):
    id: Optional[int] = Field(default_factory=lambda: ShortUUID(unique=True, max_length=5, alphabet=digits), primary_key=True)
    date_created: Optional[datetime] = Field(default_factory=lambda: datetime.now())

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