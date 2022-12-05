from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .core.config import settings
from .api.page.home import page_router

from .db.session import engine
from .db.base import Base


def include_router(app):
    app.include_router(page_router)


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
