from sqlmodel import SQLModel, Field


class RegistrationsBase(SQLModel):
    username: str
    name: str
    event_id: int


# Modello relazionale (dati non validati -> table=True)
class Registrations(RegistrationsBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
