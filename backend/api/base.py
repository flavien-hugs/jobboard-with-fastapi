from fastapi import APIRouter

from .version1 import route_users, route_pages


api_router = APIRouter()

api_router.include_router(route_pages.pages_router, prefix="", tags=["pages"])
api_router.include_router(route_users.users_router, prefix="/users", tags=["users"])
