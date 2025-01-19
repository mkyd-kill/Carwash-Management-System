from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .database import create_database, engine
from sqlmodel import Session
from contextlib import asynccontextmanager
from typing import Annotated
from datetime import datetime, UTC

# create the database on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_database()
    yield

# getting sessions
def get_session():
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()

app = FastAPI(lifespan=lifespan)

# setting up the static dir
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# setting up the template dir
templates = Jinja2Templates(directory="frontend/templates")

templates.env.globals.update(now = lambda: datetime.now(UTC))

# creating a session dependancy
SessionDependancy = Annotated[Session, Depends(get_session)]