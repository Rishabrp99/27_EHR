import uuid
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class MedicineDosage(BaseModel):
    weekly: int = Field(...)
    daily: list[str] = Field(...)


class Medicine(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    industry: str = Field(...)
    price: str = Field(...)
    manufacturing_date: datetime = Field(...)
    expiry_date: datetime = Field(...)
    effects: list[str] = Field(...)
    side_effects: list[str] = Field(...)
    storage_type: list[str] = Field(...)
    dosages: list[MedicineDosage] = Field(...)
    remarks: str = Field(...)


class MedicineUpdate(BaseModel):
    name: Optional[str]
    industry: Optional[str]
    price: Optional[str]
    manufacturing_date: Optional[datetime]
    expiry_date: Optional[datetime]
    effects: Optional[list[str]]
    side_effects: Optional[list[str]]
    storage_type: Optional[list[str]]
    dosages: Optional[list[MedicineDosage]]
    remarks: Optional[str]
