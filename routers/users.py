from data.db import DBSession
from fastapi import APIRouter, Path, Body
from fastapi.exceptions import HTTPException
from pydantic import ValidationError
from models.users import User
from sqlmodel import select, delete
from typing import Annotated


router = APIRouter()


@router.get("/users")
def get_all_users(db_session: DBSession) -> list[User]:
    try:
        users = db_session.exec(select(User)).all()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@router.get("/users/{username}")
def get_user_by_id(
    db_session: DBSession,
    username: Annotated[str, Path(description="The username of the user")],
) -> User:
    try:
        user = db_session.exec(select(User).where(
            User.username == username)).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found!")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@router.delete("/users/{username}")
def delete_user_by_id(
    db_session: DBSession,
    username: Annotated[str, Path(description="The username of the user")],
) -> str:
    try:
        statement = delete(User).where(User.username == username)
        result = db_session.exec(statement)
        db_session.commit()

        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found!")
        return "User deleted successfully!"
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@router.post("/users")
def create_user(
    db_session: DBSession,
    user: Annotated[User, Body(description="The new user")]
) -> str:
    try:
        db_session.add(User.model_validate(user))
        db_session.commit()
        return "User created!"
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.__str__())
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@router.delete("/users")
def delete_all_users(db_session: DBSession) -> str:
    try:
        statement = delete(User)
        db_session.exec(statement)
        db_session.commit()
        return "All users deleted successfully!"
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())
