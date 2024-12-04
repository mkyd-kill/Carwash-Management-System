from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .database import create_database
from contextlib import asynccontextmanager

# create the database on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_database()
    yield

app = FastAPI(lifespan=lifespan)

# setting up the static dir
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# setting up the template dir
templates = Jinja2Templates(directory="frontend/templates")