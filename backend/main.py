from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .api.base import api_router
from .core.config import settings
from .db.base import Base
from .db.session import engine
from .webapps.base import webapp_router


def include_router(app):
    app.include_router(api_router)
    app.include_router(webapp_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="backend/static"), name="static")


def create_tables():
    print("create database tables")
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    create_tables()
    return app


app = start_application()
