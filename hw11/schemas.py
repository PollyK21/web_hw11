from datetime import date
from pydantic import BaseModel, Field


class ContactModel(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: str = Field(max_length=100)
    phone: str = Field(max_length=100)
    birthday: date


class ContactResponse(ContactModel):
    id: int

    class Config:
        orm_mode = True
