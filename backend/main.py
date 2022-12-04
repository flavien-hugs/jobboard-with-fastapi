from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJEC_NAME, version=settings.PROJECT_VERSION)


@app.get("/")
def hello_api():
    response = {"msg": "Hello API"}
    return response
