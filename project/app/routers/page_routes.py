# app/routers/page_routes.py

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(
    tags=["Page Router"]
)

templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/signup")
def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@router.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/dashboard")
def dashboard_page(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@router.get("/admin-page")
def admin_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})


@router.get("/admin/register")
def admin_register_page(request: Request):
    return templates.TemplateResponse("adminSignup.html", {"request": request})

@router.get("/admin/signIn")
def admin_register_page(request: Request):
    return templates.TemplateResponse("adminLogin.html", {"request": request})

@router.get("/admin/profile")
def admin_ashboard_page(request: Request):
    return templates.TemplateResponse("adminDashboard.html", {"request": request})





@router.get("/admin/create-new-user")
def admin_create_new_user(request: Request):
    return templates.TemplateResponse("AdminCreates.html", {"request": request})