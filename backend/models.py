from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime
from shortuuid import ShortUUID
from string import digits

class Clients(SQLModel, table=True):
    client_id: Optional[int] = Field(default_factory=lambda: ShortUUID(unique=True, max_length=5, alphabet=digits), primary_key=True)
    date_created: Optional[datetime] = Field(default_factory=lambda: datetime.now())
    vehicle: str = Field(nullable=False)

class Staff(SQLModel, table=True):
    staff_id: Optional[int] = Field(default_factory=lambda: ShortUUID(unique=True, max_length=5, alphabet=digits), primary_key=True)
    date_created: Optional[datetime] = Field(default_factory=lambda: datetime.now())
    name: str = Field(nullable=False)

class Transaction(SQLModel, table=True):
    transaction_id: Optional[int] = Field(default_factory=lambda: ShortUUID(unique=True, max_length=5, alphabet=digits), primary_key=True)
    date_created: Optional[datetime] = Field(default_factory=lambda: datetime.now())
    vehicle: str = Field(nullable=False)

class Report(SQLModel, table=True):
    report_id: Optional[int] = Field(default_factory=lambda: ShortUUID(unique=True, max_length=5, alphabet=digits), primary_key=True)
    date_created: Optional[datetime] = Field(default_factory=lambda: datetime.now())
    report_type: str = Field(nullable=False)