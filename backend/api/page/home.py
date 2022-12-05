from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

TEMPLATE_DIR = str("backend/templates")

templates = Jinja2Templates(directory=TEMPLATE_DIR)
page_router = APIRouter()


@page_router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("pages/home.html", context)
