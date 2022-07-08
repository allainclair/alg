from typing import Optional

from pydantic import BaseModel


class Address(BaseModel):
    city: str
    country: str
    line1: str
    postal_code: str
    state: str

    line2: Optional[str] = None


class BasicProfile(BaseModel):
    name: str
    surname: str
    plan: str
    visibility: str
    availability: str


class Profile(BaseModel):
    id: str
    employer: str

    full_name: str
    first_name: str
    last_name: str

    address: Address

    account: Optional[str] = None
    birth_date: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    picture_url: Optional[str] = None
