from fastapi import APIRouter
from data.db import DBSession
from models.users import User
from sqlmodel import select, delete
from fastapi.exceptions import HTTPException
from typing import Annotated
from pathlib import Path


router = APIRouter()


@router.get("/users")
def get_all_users(db_session: DBSession):
    users = db_session.exec(select(User)).all()
    return users


@router.get("/users/{username}")
def get_user_by_id(
    db_session: DBSession,
    username: Annotated[str, Path(description="The username of the user")],
):
    user = db_session.exec(select(User).where(
        User.username == username)).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found!")
    return user


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
