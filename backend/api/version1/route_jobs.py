from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from backend.api.version1.route_login import get_current_user_from_token
from backend.db.models.users import User
from backend.db.repository.jobs import create_new_job
from backend.db.repository.jobs import delete_job_by_id
from backend.db.repository.jobs import list_jobs
from backend.db.repository.jobs import retreive_job
from backend.db.repository.jobs import update_job_by_id
from backend.db.session import get_db
from backend.schemas.jobs import JobCreate
from backend.schemas.jobs import ShowJob


job_router = APIRouter()


@job_router.post("/create/", summary="Create job", response_model=ShowJob)
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    user_id = current_user.id
    job = create_new_job(job=job, db=db, job_owner_id=user_id)
    return job


@job_router.get("/get/{id}/", summary="Get job", response_model=ShowJob)
def read_job(id: int, db: Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with this id {id} does not exist",
        )
    return job


@job_router.get("/all/", summary="Get all jobs", response_model=List[ShowJob])
def read_jobs(db: Session = Depends(get_db)):
    jobs = list_jobs(db=db)
    return jobs


@job_router.put("/update/{id}/", summary="Update job", response_model=List[ShowJob])
def update_job(
    id: int,
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    job_owner_id = current_user.id
    job_retrieved = retreive_job(id=id, db=db)
    if not job_retrieved:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with id {id} does not exist",
        )
    if job_retrieved.job_owner_id == current_user.id or current_user.is_superuser:
        update_job_by_id(id=id, job=job, db=db, job_owner_id=job_owner_id)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not authorized to update.",
        )
    return {"detail": "Successfully updated data."}


@job_router.delete("/delete/{id}/", summary="Delete job", response_model=List[ShowJob])
def delete_job(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    job = retreive_job(id=id, db=db)
    if not job:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with {id} does not exist",
        )

    if job.job_owner_id == current_user.id or current_user.is_superuser:
        delete_job_by_id(id=id, db=db, job_owner_id=current_user.id)
        return {"msg": "Job successfully deleted."}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not permitted !"
    )
