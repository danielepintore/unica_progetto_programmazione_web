from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
    username: str
    name: str
    email: str


class User(UserBase, table=True):  # Modello relazionale (dati non validati -> table=True)
       id: int | None = Field(default=None, primary_key=True)
