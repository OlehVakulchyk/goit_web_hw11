import re

from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field, validator


class UserModel(BaseModel):
    name: str = Field(max_length=25)
    surname: str = Field(max_length=25)
    email: EmailStr
    phone: str
    bithday: date
    information: str = Field('', max_length=250)

    @validator("phone")
    def phone_number(cls, v):
        match = re.match(r"\+380\(\d{2}\)\d{3}-\d-\d{3}|\+380\(\d{2}\)\d{3}-\d{2}-\d{2}", v)
        if (match is None) or (len(v) != 17):
            raise ValueError("Phone number must have sign '+' and 12 digits")
        return v

class UserResponse(UserModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
