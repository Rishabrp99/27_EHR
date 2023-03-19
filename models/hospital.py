"""
reference types for hospital

import { Address } from "."
import { BranchStats, BranchStaff } from "./branches"


export default interface Hospital{
    _id: string
    name: string
    established: Date
    pharmacies?: string[]
    stats: BranchStats
    staff: BranchStaff
    branches?: string[]
    address: Address
    phone: string
    email: string
}

"""

import uuid
from pydantic import BaseModel, Field
from datetime import date, datetime
from models.common import Address


class Hospital(BaseModel):

    # TODO - add stats and staff field

    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    phone: str = Field(...)
    email: str = Field(...)
    established: date = Field(...)
    pharmacy: list[str] = Field(...)
    branch: list[str] = Field(...)
    address: Address = Field(...)
