from fastapi import APIRouter
from data.db import DBSession
from sqlmodel import select
from models.events import Event

router = APIRouter()


@router.get("/events")
def example_handler(db_session: DBSession):
    events = db_session.exec(select(Event)).all()
    return events
