from icecream import ic
from sqlmodel import select, Session

from dbmodel.index import Index
from db.app import engine


def create(new_index: Index):
    print()
    ic(new_index)
    ic(type(new_index))
    # TODO: Add DB model restriction to unique NAMES for Indexes.
    if _get_by_attributes(new_index):
        return False
    else:
        # TODO: Ignoring new_index.id. Decide after what to do if the id exists.
        return _add(new_index)


def get(index_id: int):
    return _get_by_id(index_id)


def get_all():
    with Session(engine) as session:
        statement = select(Index)
        index_models = session.exec(statement)
        return [Index(**dict(index)) for index in index_models.all()]


def delete(index_id: int):
    with Session(engine) as session:
        index_model = _get_by_id(index_id)
        if index_model:
            session.delete(index_model)
            session.commit()
            return Index(**dict(index_model))
    return False


def update(index_id: int, update_index: Index):
    with Session(engine) as session:
        index_model = _get_by_id(index_id)
        if index_model:
            del update_index.id  # Ignore ID. TODO: think about this decision.
            index_model = _update_model(index_model, update_index)
            session.add(index_model)
            session.commit()
            return Index(**dict(update_index, id=index_model.id))
    return False


def _add(new_index: Index):
    with Session(engine) as session:
        index_model = Index(**dict(new_index))
        session.add(index_model)
        session.commit()
        return Index(**dict(new_index, id=index_model.id))


def _get_by_attributes(index: Index):
    with Session(engine) as session:
        statement = select(Index).where(
            Index.name == index.name
            and Index.value == index.value
        )
        index_model = session.exec(statement).first()
        return index_model


def _get_by_id(index_id: int):
    with Session(engine) as session:
        statement = select(Index).where(Index.id == index_id)
        index_model = session.exec(statement).first()
        return index_model


def _update_model(index_to_update, new_index):
    for attr, value in dict(new_index).items():
        setattr(index_to_update, attr, value)
    return index_to_update
