from fastapi import APIRouter, Path, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import select
from pathlib import Path as PPath
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


templates = Jinja2Templates(directory=(PPath(__file__).parent.parent / "templates"))


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html",
    )


@router.get("/events_list", response_class=HTMLResponse)
async def events_list(request: Request):
    return templates.TemplateResponse(
        request=request, name="events.html",
    )


@router.get("/event_detail/{id}", response_class=HTMLResponse)
async def event_detail(request: Request, id: int):
    return templates.TemplateResponse(
        request=request, name="event_detail.html",
        context={"event_id": id},
    )


@router.get("/users_list", response_class=HTMLResponse)
async def users_list(request: Request):
    return templates.TemplateResponse(
        request=request, name="users.html"
    )
