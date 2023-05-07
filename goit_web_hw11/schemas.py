import re

from datetime import datetime, date
from pydantic import BaseModel, EmailStr, Field, validator


class UserModel(BaseModel):
    name: str = Field(max_length=25)
    surname: str = Field(max_length=25)
    email: EmailStr
    phone: str = Field(example="+380(xx)xxx-xx-xx or +380(xx)xxx-x-xxx")
    bithday: date
    information: str = Field('', max_length=250)

    @validator("phone")
    def phone_number(cls, v):
        match = re.match(r"\+380\(\d{2}\)\d{3}-\d-\d{3}|\+380\(\d{2}\)\d{3}-\d{2}-\d{2}", v)
        if (match is None) or (len(v) != 17):
            raise ValueError("Phone number must be in the format '+380(хх)ххх-х-ххх' or '+380(хх)ххх-хх-хх'")
        return v

class UserResponse(UserModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
