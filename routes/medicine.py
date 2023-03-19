from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models.medicine import Medicine,MedicineUpdate

router = APIRouter()

@router.post("/medicine/", response_description="Create a new medicine", status_code=status.HTTP_201_CREATED, response_model=Medicine)
def create_Medicine(request: Request, medicine: Medicine = Body(...)):
    medicine = jsonable_encoder(medicine)
    new_medicine = request.app.database["medicines"].insert_one(medicine)
    created_medicine = request.app.database["medicines"].find_one(
        {"_id": new_medicine.inserted_id}
    )

    return created_medicine

@router.get("/medicine/{id}", response_description="Get a single medicine by id", response_model=Medicine)
def find_Medicine(id: str, request: Request):
    if (medicine := request.app.database["medicines"].find_one({"_id": id})) is not None:
        return medicine
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Medicine with ID {id} not found")

@router.put("/medicine/{id}", response_description="Update a medicine", response_model=Medicine)
def update_medicine(id: str, request: Request, medicine: MedicineUpdate = Body(...)):
    medicine = {k: v for k, v in medicine.dict().items() if v is not None}
    if len(medicine) >= 1:
        update_result = request.app.database["medicines"].update_one(
            {"_id": id}, {"$set": medicine}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"medicine with ID {id} not found")

    if (
        existing_medicine:= request.app.database["medicines"].find_one({"_id": id})
    ) is not None:
        return existing_medicine

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Medicine with ID {id} not found")

@router.delete("/medicine/{id}", response_description="Delete a medicine")
def delete_medicine(id: str, request: Request, response: Response):
    delete_result = request.app.database["medicines"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"medicine with ID {id} not found")