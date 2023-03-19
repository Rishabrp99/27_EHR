from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models.progress_note import ProgressNote,ProgressNoteUpdate

router = APIRouter()

@router.post("/progress/", response_description="Create a new progress_note", status_code=status.HTTP_201_CREATED, response_model=ProgressNote)
def create_progress_note(request: Request, progress_note: ProgressNote = Body(...)):
    print(progress_note)
    progress_note = jsonable_encoder(progress_note)
    new_progress_note = request.app.database["progress_notes"].insert_one(progress_note)
    created_progress_note = request.app.database["progress_notes"].find_one(
        {"_id": new_progress_note.inserted_id}
    )

    return created_progress_note

@router.get("/progress/{id}", response_description="Get a single progress_note by id", response_model=ProgressNote)
def find_progress_note(id: str, request: Request):
    if (progress_note := request.app.database["progress_notes"].find_one({"_id": id})) is not None:
        return progress_note
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"progress_note with ID {id} not found")

@router.put("/progress/{id}", response_description="Update a progress_note", response_model=ProgressNote)
def update_progress_note(id: str, request: Request, progress_note: ProgressNoteUpdate = Body(...)):
    progress_note = {k: v for k, v in progress_note.dict().items() if v is not None}
    if len(progress_note) >= 1:
        update_result = request.app.database["progress_notes"].update_one(
            {"_id": id}, {"$set": progress_note}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"progress_note with ID {id} not found")

    if (
        existing_progress_note:= request.app.database["progress_notes"].find_one({"_id": id})
    ) is not None:
        return existing_progress_note

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"progress_note with ID {id} not found")

@router.delete("/progress/{id}", response_description="Delete a progress_note")
def delete_progress_note(id: str, request: Request, response: Response):
    delete_result = request.app.database["progress_notes"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"progress_note with ID {id} not found")