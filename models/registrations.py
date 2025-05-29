from sqlmodel import SQLModel, Field


class RegistrationsBase(SQLModel):
    name: str


# Modello relazionale (dati non validati -> table=True)
class Registrations(RegistrationsBase, table=True):
    username: str = Field(default=None, primary_key=True)
    event_id: int = Field(default=None, primary_key=True)
