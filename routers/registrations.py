from fastapi import APIRouter, Path, HTTPException
from data.db import DBSession
from models.registrations import Registrations
from sqlmodel import select, delete

router = APIRouter()


@router.get("/registrations")
def get_all_registrations(db_session: DBSession):
    registrations = db_session.exec(select(Registrations)).all()
    return registrations
