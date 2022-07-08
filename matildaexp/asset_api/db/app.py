from sqlmodel import create_engine, SQLModel, Session
from dbmodel.index import Index
from dbmodel.asset import Asset

from db.path import db_path


def start():
    eng = create_engine(db_path)
    SQLModel.metadata.create_all(eng)
    return eng


engine = start()


def add(instance):
    with Session(engine) as session:
        session.add(instance)
        session.commit()
