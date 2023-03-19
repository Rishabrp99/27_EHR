from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models.industry import Industry,IndustryUpdate

router = APIRouter()

@router.post("/industry/", response_description="Create a new industry", status_code=status.HTTP_201_CREATED, response_model=Industry)
def create_industry(request: Request, industry: Industry = Body(...)):
    print(industry)
    industry = jsonable_encoder(industry)
    new_industry = request.app.database["industrys"].insert_one(industry)
    created_industry = request.app.database["industrys"].find_one(
        {"_id": new_industry.inserted_id}
    )

    return created_industry

@router.get("/industry/{id}", response_description="Get a single industry by id", response_model=Industry)
def find_industry(id: str, request: Request):
    if (industry := request.app.database["industrys"].find_one({"_id": id})) is not None:
        return industry
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"industry with ID {id} not found")

@router.put("/industry/{id}", response_description="Update a industry", response_model=Industry)
def update_industry(id: str, request: Request, industry: IndustryUpdate = Body(...)):
    industry = {k: v for k, v in industry.dict().items() if v is not None}
    if len(industry) >= 1:
        update_result = request.app.database["industrys"].update_one(
            {"_id": id}, {"$set": industry}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"industry with ID {id} not found")

    if (
        existing_industry:= request.app.database["industrys"].find_one({"_id": id})
    ) is not None:
        return existing_industry

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"industry with ID {id} not found")

@router.delete("/industry/{id}", response_description="Delete a industry")
def delete_industry(id: str, request: Request, response: Response):
    delete_result = request.app.database["industrys"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"industry with ID {id} not found")