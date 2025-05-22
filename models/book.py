from sqlmodel import SQLModel, Field
from typing import Annotated


class BookBase(SQLModel):  # Superclasse con attibuti comuni
    title: str
    author: str
    review: Annotated[int | None, Field(ge=1, le=5)] = None


class Book(BookBase, table=True):  # Modello relazionale (dati non validati -> table=True)
    id: int = Field(default=None, primary_key=True)


class BookCreate(BookBase):  # Schema usato per creare un libro
    pass


class BookPublic(BookBase):  # Schema restituito dall'api
    id: int
