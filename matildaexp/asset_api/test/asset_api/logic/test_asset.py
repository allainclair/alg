from pytest import fixture

from dbmodel.asset import Asset
from dbmodel.index import Index
from logic.asset import create
from logic.asset import get
from logic.index import create as create_index
# from logic.asset import get_all
# from logic.asset import assets

from db.app import (
    start as db_start,
)

from test.db.db_delete import delete as db_delete


asset_0 = Asset(name='Asset 0', ir=0.2, fix_interest=0.05, duration=1, id_index=1)
index_0 = Index(name='Index 0', value=0.1)


def _start_db():
    db_delete()
    db_start()


def test_create_one_without_id():
    _start_db()

    created_asset = create(asset_0)
    assert asset_0.id is None
    assert created_asset.id is not None


def test_get_ok():
    _start_db()
    created_asset = create(asset_0)
    created_index = create_index(index_0)
    assert get(created_asset.id) == created_asset


# @fixture
# def reset_assets():
#     del assets[:]
#
#
# def test_create_a_asset_without_id(reset_assets):
#     asset = Asset(name='Asset 0', ir=0.15, fix_interest=0.5, duration=1, id_index=1)
#
#     created_asset = create(asset)
#     asset.id = len(test_assets)
#     assert created_asset == asset
#
#     test_assets.append(created_asset)
#
#
# def test_create_assets_without_id():
#     asset1 = Asset(name='Asset 1', ir=0.15, fix_interest=0.5, duration=1, id_index=2)
#     created_asset1 = create(asset1)
#     asset1.id = len(test_assets)
#     assert created_asset1 == asset1
#     test_assets.append(asset1)
#
#     asset2 = Asset(name='Asset 2', ir=0.20, fix_interest=0.5, duration=1, id_index=3)
#     created_asset2 = create(asset2)
#     asset2.id = len(test_assets)
#     assert created_asset2 == asset2
#     test_assets.append(created_asset2)
#
#
# def test_create_asset_already_exists():
#     asset = Asset(name='Asset 0', ir=0.15, fix_interest=0.5, duration=1, id_index=1)
#     assert not create(asset)
#
#
# def test_get_assets():
#     assert get_all() == test_assets
#
#
# def test_get_asset_ok():
#     asset = test_assets[0]
#     assert get(asset.id) == asset
#
#
# def test_get_asset_wrong_id():
#     assert not get('wrong_id')
