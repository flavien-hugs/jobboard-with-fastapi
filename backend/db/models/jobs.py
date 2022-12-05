from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from ..base_class import Base


class Job(Base):
    job_id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String, nullable=False)
    job_company = Column(String, nullable=False)
    job_company_url = Column(String)
    job_location = Column(String, nullable=False)
    job_description = Column(String, nullable=False)
    job_date_posted = Column(Date)
    job_is_active = Column(Boolean(), default=True)
    job_owner_id = Column(Integer, ForeignKey("user.id"))
    job_owner = relationship("User", back_populates="jobs")
