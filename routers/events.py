from data.db import DBSession
from fastapi import APIRouter, Path, Body, HTTPException
from pydantic import ValidationError
from models.events import Event, EventCreate
from models.registrations import Registrations
from models.users import User
from sqlmodel import select, delete
from typing import Annotated

router = APIRouter()


@router.get("/events")
def get_all_events(db_session: DBSession) -> list[Event]:
    try:
        events = db_session.exec(select(Event)).all()
        return events
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@router.post("/events")
def create_event(
    db_session: DBSession,
    event: Annotated[Event, Body(description="The new event")]
) -> str:
    try:
        event.id = None  # let the database generate an id
        db_session.add(Event.model_validate(event))
        db_session.commit()
        return "Event created successfully!"
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.__str__())
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@router.delete("/events")
def delete_all_events(db_session: DBSession) -> str:
    try:
        db_session.exec(delete(Event))
        db_session.commit()
        return "All events deleted successfully!"
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@router.get("/events/{id}")
def get_event_with_id(
    db_session: DBSession,
    id: Annotated[int, Path(description="The id of the event")]
) -> Event:
    try:
        event = db_session.get(Event, id)
        if event:
            return event
        else:
            raise HTTPException(status_code=404, detail="Event not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@router.put("/events/{id}")
def update_event(
    db_session: DBSession,
    id: Annotated[int, Path(description="The id of the event to update")],
    new_event: EventCreate
) -> str:
    try:
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
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@router.delete("/events/{id}")
def delete_event(
    db_session: DBSession,
    id: Annotated[int, Path(description="The id of the event to delete")]
) -> str:
    try:
        event = db_session.get(Event, id)
        if event is None:
            raise HTTPException(status_code=404, detail="Event not found")
        db_session.delete(event)
        db_session.commit()
        return "Event deleted successfully!"
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@router.post("/events/{id}/register")
def add_registration(
    db_session: DBSession,
    id: Annotated[int, Path(description="The id of the event to delete")],
    user: Annotated[User, Body(description="The user to register")]
) -> str:
    try:
        registration = Registrations(
            username=user.username, name=user.name, event_id=id)
        db_session.add(Registrations.model_validate(registration))
        db_session.commit()
        return "Registration successfull!"
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())
