from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models.prescription import Prescription,PrescriptionUpdate

router = APIRouter()

@router.post("/prescription/", response_description="Create a new prescription", status_code=status.HTTP_201_CREATED, response_model=Prescription)
def create_Patient(request: Request, prescription: Prescription = Body(...)):
    prescription = jsonable_encoder(prescription)
    new_precription = request.app.database["prescriptions"].insert_one(prescription)
    created_prescription = request.app.database["prescriptions"].find_one(
        {"_id": new_precription.inserted_id}
    )
    return created_prescription

@router.get("/prescription/{id}", response_description="Get a single prescription by id", response_model=Prescription)
def find_Patient(id: str, request: Request):
    if (Prescription := request.app.database["prescriptions"].find_one({"_id": id})) is not None:
        return Prescription
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Prescription with ID {id} not found")

@router.put("/prescription/{id}", response_description="Update a existing prescription", response_model=Prescription)
def update_patient(id: str, request: Request, prescription: Prescription = Body(...)):
    patient = {k: v for k, v in patient.dict().items() if v is not None}
    if len(patient) >= 1:
        update_result = request.app.database["prescriptions"].update_one(
            {"_id": id}, {"$set": prescription}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"prescription with ID {id} not found")

    if (
        existing_prescription:= request.app.database["prescriptions"].find_one({"_id": id})
    ) is not None:
        return existing_prescription

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Patient with ID {id} not found")

@router.delete("/prescription/{id}", response_description="Delete a prescription")
def delete_patient(id: str, request: Request, response: Response):
    delete_result = request.app.database["prescriptions"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"prescription with ID {id} not found")