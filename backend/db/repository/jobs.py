from sqlalchemy.orm import Session
from backend.db.models.jobs import Job
from backend.schemas.jobs import JobCreate


def retreive_job(id: int, db: Session):
    item = db.query(Job).filter(Job.id == id).first()
    return item


def create_new_job(job: JobCreate, db: Session, job_owner_id: int):
    job_object = Job(**job.dict(), job_owner_id=job_owner_id)
    db.add(job_object)
    db.commit()
    db.refresh(job_object)
    return job_object
