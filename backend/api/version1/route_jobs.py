from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from backend.db.repository.jobs import create_new_job
from backend.db.repository.jobs import list_jobs
from backend.db.repository.jobs import retreive_job
from backend.db.repository.jobs import update_job_by_id
from backend.db.session import get_db
from backend.schemas.jobs import JobCreate
from backend.schemas.jobs import ShowJob


job_router = APIRouter()


@job_router.post("/create/", response_model=ShowJob)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    current_user = 1
    job = create_new_job(job=job, db=db, job_owner_id=current_user)
    return job


@job_router.post("/get/{id}/", response_model=ShowJob)
def read_job(id: int, db: Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with this id {id} does not exist",
        )
    return job


@job_router.post("/all", response_model=ShowJob)
def read_jobs(db: Session = Depends(get_db)):
    jobs = list_jobs(db=db)
    return jobs


@job_router.put("/update/{id}")
def update_job(id: int, job: JobCreate, db: Session = Depends(get_db)):
    current_user = 1
    message = update_job_by_id(id=id, job=job, db=db, job_owner_id=current_user)
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with id {id} not found"
        )
    return {"message": "Successfully updated data."}
