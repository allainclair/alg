from fastapi import FastAPI
from fastapi import HTTPException

from icecream import ic

from route_v1 import (
    ASSETS,
    ASSET,
    INDEXES,
    INDEX,
)

from dbmodel.index import Index
from dbmodel.asset import Asset

# from api_model.asset import Asset
# from api_model.index import Index

from logic.asset import create as asset_create
# from logic.asset import get_all as asset_get_all
from logic.asset import get as asset_get

from logic.index import create as index_create
from logic.index import get_all as index_get_all
from logic.index import get as index_get
from logic.index import update as index_update
from logic.index import delete as index_delete

from exception_detail import (
    ASSET_ALREADY_EXISTS,
    ASSET_NOT_FOUND,
    INDEX_ALREADY_EXISTS,
    INDEX_NOT_FOUND,
)

app = FastAPI()


@app.get('/')
def hello_world():
    return {'Hello': 'World'}


# Assets

@app.post(f'/{ASSETS}')
def create_asset(asset: Asset):
    if asset_create(asset):
        return asset
    else:
        raise HTTPException(
            status_code=ASSET_ALREADY_EXISTS.status_code,
            detail=ASSET_ALREADY_EXISTS.detail,
        )


# @app.get(f'/{ASSETS}')
# def get_assets():
#     # We need to handle database errors in the future.
#     return asset_get_all()


@app.get(f'/{ASSET}/{{asset_id}}', response_model=Asset)
def get_asset(asset_id: int):
    asset = asset_get(asset_id)
    if asset:
        return asset
    else:
        raise HTTPException(
            status_code=ASSET_NOT_FOUND.status_code,
            detail=ASSET_NOT_FOUND.detail,
        )


# Indexes

@app.post(f'/{INDEXES}')
def create_index(index: Index):
    print()
    ic(index)
    ic(type(index))
    if index_create(index):
        return index
    else:
        raise HTTPException(
            status_code=INDEX_ALREADY_EXISTS.status_code,
            detail=INDEX_ALREADY_EXISTS.detail,
        )


@app.get(f'/{INDEXES}')
def get_indexes():
    # We need to handle database errors in the future.
    indexes = index_get_all()
    ic(indexes)
    return indexes


@app.get(f'/{INDEX}/{{index_id}}', response_model=Index)
def get_index(index_id: int):
    index = index_get(index_id)
    if index:
        return index
    else:
        raise HTTPException(
            status_code=INDEX_NOT_FOUND.status_code,
            detail=INDEX_NOT_FOUND.detail,
        )


@app.delete(f'/{INDEX}/{{index_id}}', response_model=Index)
def update_index(index_id: int):
    index = index_delete(index_id)
    if index:
        return index
    else:
        raise HTTPException(
            status_code=INDEX_NOT_FOUND.status_code,
            detail=INDEX_NOT_FOUND.detail,
        )


@app.put(f'/{INDEX}/{{index_id}}', response_model=Index)
def update_index(index_id: int, index: Index):
    index = index_update(index_id, index)
    if index:
        return index
    else:
        raise HTTPException(
            status_code=INDEX_NOT_FOUND.status_code,
            detail=INDEX_NOT_FOUND.detail,
        )
