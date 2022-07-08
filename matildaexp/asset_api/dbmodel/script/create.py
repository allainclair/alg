from sqlmodel import SQLModel, create_engine

from dbmodel.index import Index
from dbmodel.asset import Asset


if __name__ == '__main__':
    path = 'db'
    print('Creating DB..')
    engine = create_engine(f'sqlite:///{path}/database.db')
    SQLModel.metadata.create_all(engine)
    print(f'DB created at: {path}/')
