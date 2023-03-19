
import uuid
from datetime import date, datetime, time, timedelta
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum
from models.common import Address


# Enums

class BloodGroup(str, Enum):

    A_POSITIVE = "A+"
    B_NEGATIVE = "B+"
    O_POSITIVE = "O+"
    A_NEGATIVE = "A-"
    B_POSITIVE = "B-"
    O_NEGATIVE = "O-"
    AB_POSITIVE = "AB+"
    AB_NEGATIVE = "AB-"
    OTHER = "other"


class PatientSymptomSeverity(str, Enum):

    LOW = "low"
    MEDIUM = "medium"
    NORMAL = "normal"
    HIGH = "high"


class TemperatureScale(str, Enum):

    C = "c"
    F = "f"


class Gender(str, Enum):

    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


# Enums End


# Model Classes
# TODO : Add validation for the fields in classes

class PatientSymptom(BaseModel):

    name: str = Field(...)
    description: str = Field(...)
    severity: PatientSymptomSeverity = Field(...)


class PatientAdmission(BaseModel):

    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    date_time: datetime = Field(alias="datetime")
    hospital: str = Field(...)


class PatientGuardian(BaseModel):

    name: str = Field(...)
    phone: str = Field(...)
    relation: str = Field(default="other")


class Temperature(BaseModel):

    value: int = Field(...)
    scale: TemperatureScale | None = Field(default=None)


class BloodPressure(BaseModel):

    high: int = Field(...)
    low: int = Field(...)


class BloodTest(BaseModel):

    rbc_count: int = Field(...)
    wbc_count: int = Field(...)
    platelet_count: int = Field(...)
    haemoglobin: int = Field(...)


class UrineTest(BaseModel):

    pH: int = Field(...)
    specific_gravity: int = Field(...)
    glucose: str = Field(...)
    ketones: list[str] = Field(...)


class Doctor(BaseModel):

    id: str = Field(...)
    Date: date = Field(alias="date")


class PatientCheckup(BaseModel):

    admission: str = Field(...)
    temperature: Temperature = Field(...)
    blood_pressure: BloodPressure = Field(...)
    blood_test: BloodTest | None = Field(default=None)
    urine_test: UrineTest | None = Field(default=None)


class Patient(BaseModel):

    # TODO: Implementing ABHA card, aadhar card

    id: str = Field(...)
    name: str = Field(...)
    gender: Gender = Field(...)
    emergency_contact : str = Field(...)
    phone: str = Field(...)
    age :str
    address: str = Field(...)
    dob: date = Field(...)
    blood_group: str = Field(...)
    height:str
    weight : str


class PatientUpdate(BaseModel):
    name: Optional[str] 
    gender: Optional[Gender] 
    phone: Optional[str] 
    email: Optional[str] 
    age : Optional[str]
    dob: Optional[date] 
    address : Optional[str]
    blood_group: Optional[str]
    height :Optional[str]
    weight : Optional[str]

