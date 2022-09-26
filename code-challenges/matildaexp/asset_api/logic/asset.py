"""Change module to database"""
from icecream import ic
from sqlmodel import select, Session

from dbmodel.asset import Asset
from dbmodel.index import Index

from api_model.asset import Asset

from db.app import engine


def create(new_asset: Asset):
    # TODO: Add DB model restriction to unique NAMES for Indexes.
    if _get_by_attributes(new_asset):
        return False
    else:
        # TODO: Ignoring new_index.id. Decide after what to do if the id exists.
        return _add(new_asset)


def get(asset_id: int):
    with Session(engine) as session:
        statement = select(Asset, Index).where(
            Asset.id == asset_id
            and Asset.id_index == Index.id
        )
        models = session.exec(statement).first()
        ic(models)
        # ic(models.Asset.id)
        # ic(models.Index)
        return models


# def get_all():
#     return assets


def _get_by_attributes(asset: Asset):
    with Session(engine) as session:
        statement = select(Asset).where(
            Asset.name == asset.name
            and Asset.ir == asset.ir
            and Asset.fix_interest == asset.fix_interest
            and Asset.duration == asset.duration
            and Asset.id_index == asset.id_index
        )
        asset_model = session.exec(statement).first()
        return asset_model


def _add(new_asset: Asset):
    with Session(engine) as session:
        asset_model = Asset(**dict(new_asset))
        session.add(asset_model)
        session.commit()
        return Asset(**dict(new_asset, id=asset_model.id))
