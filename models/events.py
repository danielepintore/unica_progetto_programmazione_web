from sqlmodel import SQLModel, Field
from datetime import datetime
from pydantic import Field as PyField
from pydantic import field_validator


class EventBase(SQLModel):  # Superclasse con attibuti comuni
    title: str = PyField(min_length=3)
    description: str = PyField(min_length=3)
    date: datetime = PyField(strict=True)
    location: str = PyField(min_length=3)

    @field_validator('date', mode='before')
    @classmethod
    def parse_custom_datetime(cls, v):
        if isinstance(v, str):
            try:
                return datetime.strptime(v, '%Y-%m-%dT%H:%M')
            except ValueError:
                raise ValueError('Datetime must be in format YYYY-MM-DDTHH:MM')
        return v


# Modello relazionale (dati non validati -> table=True)
class Event(EventBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class EventCreate(EventBase):
    pass
