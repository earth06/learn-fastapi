from urllib.parse import urlencode

from fastapi import APIRouter, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/web/templates")

@router.get("/")
def index(request: Request):
    return templates.TemplateResponse(request,"index.html")

@router.post("/login")
def login(username: str = Form()):
    return {"user_name": username} 

