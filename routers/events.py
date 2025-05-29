from fastapi import APIRouter, Path, HTTPException
from fastapi.exceptions import HTTPException
from data.db import DBSession
from sqlmodel import select, delete
from pathlib import Path
from models.events import Event, EventCreate
from models.users import UserBase
from models.registrations import Registrations
from typing import Annotated

router = APIRouter()


@router.get("/events")
def get_all_events(db_session: DBSession):
    events = db_session.exec(select(Event)).all()
    return events


@router.post("/events")
def create_event(db_session: DBSession, event: Event):
    event.id = None
    db_session.add(Event.model_validate(event))
    db_session.commit()
    return "Event created successfully!"


@router.delete("/events")
def delete_all_events(db_session: DBSession):
    statement = delete(Event)
    db_session.exec(statement)
    db_session.commit()
    return "All events deleted successfully!"


@router.get("/events/{id}")
def get_event_with_id(
    db_session: DBSession,
    id: Annotated[int, Path(description="The id of the event")]
) -> Event:
    event = db_session.get(Event, id)
    if event:
        return event
    else:
        raise HTTPException(status_code=404, detail="Event not found")


@router.put("/events/{id}")
def update_event(
    db_session: DBSession,
    id: Annotated[int, Path(description="The id of the event to update")],
    new_event: EventCreate
):
    event = db_session.get(Event, id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    event.title = new_event.title
    event.description = new_event.description
    event.date = new_event.date
    event.location = new_event.location
    db_session.add(event)
    db_session.commit()
    return "Event updated successfully!"


@router.delete("/events/{id}")
def delete_event(
    db_session: DBSession,
    id: Annotated[int, Path(description="The id of the event to delete")]
):
    event = db_session.get(Event, id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    db_session.delete(event)
    db_session.commit()
    return "Event deleted successfully!"


@router.post("/events/{id}/register")
def add_registration(
    db_session: DBSession,
    id: Annotated[int, Path(description="The id of the event to delete")],
    user: Annotated[UserBase, Path(description="The user to register")]
):
    registration = Registrations(
        username=user.username, name=user.name, event_id=id)
    db_session.add(Registrations.model_validate(registration))
    db_session.commit()
    return "Registration successfull!"
