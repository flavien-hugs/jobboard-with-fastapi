from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.db.session import get_db
from backend.schemas.jobs import JobCreate, ShowJob
from backend.db.repository.jobs import create_new_job


job_router = APIRouter()


@job_router.post("/create/", response_model=ShowJob)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    current_user = 1
    job = create_new_job(job=job, db=db, job_owner_id=current_user)
    return job
