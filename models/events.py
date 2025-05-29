from sqlmodel import SQLModel, Field
from datetime import datetime
# from typing import Annotated


class EventBase(SQLModel):  # Superclasse con attibuti comuni
    title: str
    description: str
    date: datetime
    location: str


class Event(EventBase, table=True):  # Modello relazionale (dati non validati -> table=True)
    id: int | None = Field(default=None, primary_key=True)


class EventCreate(EventBase):  # Schema usato per creare un libro
    pass


"""
class BookCreate(BookBase):  # Schema usato per creare un libro
    pass


class BookPublic(BookBase):  # Schema restituito dall'api
    id: int
"""
