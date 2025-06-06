from sqlmodel import SQLModel, Field
from pydantic import Field as PyField
from pydantic import EmailStr


class UserBase(SQLModel):
    name: str = PyField(min_length=3)
    email: EmailStr = PyField(min_length=3)


# Modello relazionale (dati non validati -> table=True)
class User(UserBase, table=True):
    username: str = Field(default=None, primary_key=True, min_length=3)
