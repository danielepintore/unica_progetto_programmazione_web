from fastapi import APIRouter, Path
from fastapi.exceptions import HTTPException
from sqlmodel import select
from typing import Annotated
from models.book import Book, BookCreate
from data.db import DBSession

router = APIRouter()


@router.get("/example")
def example_handler():
    return {"status": "ok"}


@router.get("/get_example_with_db_session")
def example_handler_with_db_get(db_session: DBSession) -> list[Book]:
    """Gets all books"""
    books = db_session.exec(select(Book)).all()
    return books


@router.get("/get_example_with_db_session/{id}")
def example_handler_with_db_get_with_id(
        db_session: DBSession,
        id: Annotated[int, Path(description="The id of the book")]
) -> Book:
    """Gets all books"""
    book = db_session.get(Book, id).all()
    if book:
        return book
    else:
        raise HTTPException(status_code=404, detail="Book not found")


@router.post("/post_example_with_db_session")
def example_handler_with_db_post(
        db_session: DBSession,
        book: BookCreate
):
    """Adds a book"""
    db_session.add(Book.model_validate(book))
    db_session.commit()
    return "Book added!!"
