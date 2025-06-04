from sqlmodel import create_engine, SQLModel, Session
from fastapi import Depends
from faker import Faker
from pathlib import Path
from typing import Annotated
import os
# Remember to import all classes of database objects
from models.events import Event
from models.users import User

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
            # generate 10 events and users and add them to the db
            for i in range(10):
                event = Event(title=f.sentence(nb_words=5),
                              description=f.name(), date=f.date_time(),
                              location=f.address())
                user = User(username=f.user_name(),
                            name=f.name(), email=f.email())

                session.add(event)
                session.add(user)
            session.commit()


def get_db_session():
    with Session(engine) as session:
        yield session


DBSession = Annotated[Session, Depends(get_db_session)]
