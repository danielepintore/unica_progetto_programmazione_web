from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    username: str
    name: str
    email: str


# Modello relazionale (dati non validati -> table=True)
class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
