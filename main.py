from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from contextlib import asynccontextmanager
from routers import frontend, events, users
from data.db import init_database

API_PREFIX = "/v1"
APP_STATIC_DIR = Path(__file__).parent / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # on start
    init_database()
    yield
    # on close

app = FastAPI(lifespan=lifespan)
app.include_router(frontend.router)
app.include_router(events.router)
app.include_router(users.router)
# app.include_router(frontend.router, prefix=API_PREFIX)
app.mount("/", StaticFiles(directory=APP_STATIC_DIR, html=True), name="static")


