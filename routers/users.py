from fastapi import APIRouter
from data.db import DBSession
from models.users import User
from sqlmodel import select, delete
from typing import Annotated
from pathlib import Path


router = APIRouter()


@router.get("/users")
def get_all_users(db_session: DBSession):
    users = db_session.exec(select(User)).all()
    return users


@router.get("/users/{id}")
def get_user_by_id(
    db_session: DBSession,
    id: Annotated[int, Path(description="The id of the user")],
):
    users = db_session.get(User, id)
    return users


@router.post("/users")
def create_user(db_session: DBSession, user: User):
    user.id = None
    db_session.add(User.model_validate(user))
    db_session.commit()
    return "User created!"


@router.delete("/users")
def delete_all_users(db_session: DBSession):
    statement = delete(User)
    db_session.exec(statement)
    db_session.commit()
    return "All users deleted successfully!"
