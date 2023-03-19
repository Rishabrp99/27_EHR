import uuid
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from medicine import Medicine,MedicineDosage

class Prescription(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    date : datetime
    doctor_id:str
    patient_id:str
    medicines:list[str]
    dosages: list[MedicineDosage] = Field(...)

    