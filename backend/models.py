from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime
from shortuuid import ShortUUID
from string import digits

class BaseModel(SQLModel):
    id: Optional[int] = Field(default_factory=lambda: ShortUUID(unique=True, max_length=5, alphabet=digits), primary_key=True)
    date_created: Optional[datetime] = Field(default_factory=lambda: datetime.now())

class Clients(BaseModel):
    vehicle: str = Field(nullable=False)

class Staff(BaseModel):
    name: str = Field(nullable=False)

class Transaction(BaseModel):
    vehicle: str = Field(nullable=False)

class Report(BaseModel):
    report_type: str = Field(nullable=False)