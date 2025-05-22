from sqlmodel import create_engine, SQLModel, Session
from fastapi import Depends
from faker import Faker
from pathlib import Path
from typing import Annotated
import os
# Remember to import all classes of database objects
from models.book import Book  # NOQA

DB_PATH = Path(__file__).parent / "store.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)
DB_URL = f"sqlite:///{DB_PATH}"
connect_args = {"check_same_thread": False}
engine = create_engine(DB_URL, connect_args=connect_args, echo=True)


def init_database() -> None:
    db_exists = os.path.isfile(DB_PATH)
    SQLModel.metadata.create_all(engine)
    if not db_exists:
        # We don't have a database, generate fake data
        f = Faker("it_IT")
        with Session(engine) as session:
            # generate 100 books
            for i in range(100):
                book = Book(title=f.sentence(nb_words=5),
                            author=f.name(), rieview=f.pyint(1, 5))
                session.add(book)
            session.commit()


def get_db_session():
    with Session(engine) as session:
        yield session


DBSession = Annotated[Session, Depends(get_db_session)]
