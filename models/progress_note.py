import uuid
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class ProgressNote(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    patient: str = Field(...)
    doctor: str = Field(...)
    data: str = Field(...)
    created: datetime = Field(...)


class ProgressNoteUpdate(BaseModel):
    patient: Optional[str]
    doctor: Optional[str]
    data: Optional[str]
    created: Optional[datetime]
