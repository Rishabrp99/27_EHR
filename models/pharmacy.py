from pydantic import BaseModel,Field
import uuid
from typing import Optional
from datetime import date , datetime



class Pharmacy(BaseModel):
    id : str = Field(default_factory=uuid.uuid4, alias="_id")
    medicines : str = Field(...)
    staff : list[str] = Field(...)
    address : str =Field(...)
    phone : str = Field(...)
    email : str = Field(...)


