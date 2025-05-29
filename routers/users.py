from fastapi import APIRouter
from data.db import DBSession
from models.users import User
from sqlmodel import select, delete


router = APIRouter ()

@router.get("/users")
def get_all_users(db_session: DBSession):
    users= db_session.exec(select(User)).all()
    return users