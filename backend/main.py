from fastapi import FastAPI
from .core import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)


@app.get("/")
def hello_api():
    response = {"msg": "Hello API"}
    return response
