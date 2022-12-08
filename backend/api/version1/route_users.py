from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from backend.db.repository.users import create_new_user
from backend.db.session import get_db
from backend.schemas.users import ShowUser
from backend.schemas.users import UserCreate

users_router = APIRouter()


@users_router.post("/register/", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user
