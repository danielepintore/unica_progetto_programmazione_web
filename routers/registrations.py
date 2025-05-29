from data.db import DBSession
from fastapi import APIRouter, HTTPException
from models.registrations import Registrations
from sqlmodel import select

router = APIRouter()


@router.get("/registrations")
def get_all_registrations(db_session: DBSession):
    try:
        registrations = db_session.exec(select(Registrations)).all()
        return registrations
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())
