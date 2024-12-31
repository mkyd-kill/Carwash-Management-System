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

class Service(BaseModel):
    pass