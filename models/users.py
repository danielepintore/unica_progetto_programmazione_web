from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    name: str
    email: str


# Modello relazionale (dati non validati -> table=True)
class User(UserBase, table=True):
    username: str = Field(default=None, primary_key=True)
