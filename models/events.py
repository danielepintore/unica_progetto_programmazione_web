from sqlmodel import SQLModel, Field
from datetime import datetime
from pydantic import Field as PyField


class EventBase(SQLModel):  # Superclasse con attibuti comuni
    title: str
    description: str
    date: datetime = PyField(strict=True)
    location: str


# Modello relazionale (dati non validati -> table=True)
class Event(EventBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class EventCreate(EventBase):
    pass
