

from fastapi import FastAPI
from app.routers import user_routes,page_routes,admin_routes
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



app = FastAPI()


app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(admin_routes.router)
app.include_router(user_routes.router)
app.include_router(page_routes.router)



# Make templates accessible globally if needed
templates = Jinja2Templates(directory="templates")