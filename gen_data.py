from models.hospital import Hospital
from models.patient import Patient
from pydantic_factories import ModelFactory

class HospitalFactory(ModelFactory):
    __model__ = Hospital


class PatientFactory(ModelFactory):
    __model__ = Patient


