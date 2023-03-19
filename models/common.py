import uuid
from typing import Optional
from pydantic import BaseModel, Field


class Address(BaseModel):
    line_1: str = Field(...)
    line_2: str = Field(...)
    city_village: str = Field(...)
    state: str = Field(...)
    pin_code: str = Field(...)


class AddressUpdate(BaseModel):
    line_1: Optional[str]
    line_2: Optional[str]
    city_village: Optional[str]
    state: Optional[str]
    pin_code: Optional[str]
