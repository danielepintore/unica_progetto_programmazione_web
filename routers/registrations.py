from data.db import DBSession
from fastapi import APIRouter, HTTPException, Query
from models.registrations import Registrations
from sqlmodel import select
from typing import Annotated

router = APIRouter()


@router.get("/registrations")
def get_all_registrations(db_session: DBSession) -> list[Registrations]:
    try:
        registrations = db_session.exec(select(Registrations)).all()
        return registrations
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@router.delete("/registrations")
def delete_event(
    db_session: DBSession,
    username: Annotated[str, Query(description="The username of the user")],
    event_id: Annotated[int, Query(description="The id of the event")]
) -> str:
    try:
        query = select(Registrations).where(
            Registrations.username == username,
            Registrations.event_id == event_id
        )
        registration = db_session.exec(query).first()
        if registration is None:
            raise HTTPException(
                status_code=404, detail="Registration not found")
        db_session.delete(registration)
        db_session.commit()
        return "Registration deleted successfully!"
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())
