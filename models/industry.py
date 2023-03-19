import uuid
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from models.common import Address


class IndustryMedicine(BaseModel):
    id: str = Field(...)
    production_method: str = Field(...)


class Industry(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    phone: list[str] = Field(...)
    email: str = Field(...)
    established: datetime = Field(...)
    address: Address = Field(...)
    medicines: list[IndustryMedicine] = Field(...)


class IndustryUpdate(BaseModel):
    name: Optional[str]
    phone: Optional[list[str]]
    email: Optional[str]
    etablished: Optional[datetime]
    address: Optional[Address]
    medicines: Optional[list[IndustryMedicine]]
