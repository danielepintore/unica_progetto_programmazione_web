from fastapi import APIRouter
from data.db import DBSession
from sqlmodel import select
from models.events import Event

router = APIRouter()


@router.get("/events")
def get_all_events(db_session: DBSession):
    events = db_session.exec(select(Event)).all()
    return events

@router.post("/events")
def create_event(db_session: DBSession, event: Event):
    event.id=None
    db_session.add(Event.model_validate(event))
    db_session.commit()
    return "Event created successfully!"