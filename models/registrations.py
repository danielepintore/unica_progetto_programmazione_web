from sqlmodel import SQLModel, Field
from pydantic import Field as PyField


class RegistrationsBase(SQLModel):
    name: str = PyField(min_length=3)


# Modello relazionale (dati non validati -> table=True)
class Registrations(RegistrationsBase, table=True):
    username: str = Field(default=None, primary_key=True, min_length=3)
    event_id: int = Field(default=None, primary_key=True)


class RegistrationPublic(SQLModel):
    username: str = PyField(min_length=3)
    event_id: int
