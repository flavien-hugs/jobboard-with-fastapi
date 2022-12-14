from fastapi import APIRouter

from .version1 import route_jobs
from .version1 import route_login
from .version1 import route_users

api_router = APIRouter()

api_router.include_router(route_users.users_router, prefix="/users", tags=["users"])
api_router.include_router(route_jobs.job_router, prefix="/jobs", tags=["jobs"])
api_router.include_router(route_login.login_router, prefix="/login", tags=["login"])
