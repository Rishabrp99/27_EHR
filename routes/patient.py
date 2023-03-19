from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models.patient import Patient,PatientUpdate

router = APIRouter()

@router.post("/", response_description="Create a new patient", status_code=status.HTTP_201_CREATED, response_model=Patient)
def create_Patient(request: Request, patient: Patient = Body(...)):
    patient = jsonable_encoder(patient)
    new_patient = request.app.database["patients"].insert_one(patient)
    created_patient = request.app.database["patients"].find_one(
        {"_id": new_patient.inserted_id}
    )

    return created_patient

@router.get("/{id}", response_description="Get a single patient by id", response_model=Patient)
def find_Patient(id: str, request: Request):
    if (patient := request.app.database["patients"].find_one({"_id": id})) is not None:
        return patient
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Patient with ID {id} not found")

@router.put("/{id}", response_description="Update a patient", response_model=Patient)
def update_patient(id: str, request: Request, patient: PatientUpdate = Body(...)):
    patient = {k: v for k, v in patient.dict().items() if v is not None}
    if len(patient) >= 1:
        update_result = request.app.database["patients"].update_one(
            {"_id": id}, {"$set": patient}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"patient with ID {id} not found")

    if (
        existing_patient:= request.app.database["patients"].find_one({"_id": id})
    ) is not None:
        return existing_patient

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Patient with ID {id} not found")

@router.delete("/{id}", response_description="Delete a patient")
def delete_patient(id: str, request: Request, response: Response):
    delete_result = request.app.database["patients"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"patient with ID {id} not found")