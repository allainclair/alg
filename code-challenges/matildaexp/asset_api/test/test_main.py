from main import app

from fastapi.testclient import TestClient

from route_v1 import ASSETS
from route_v1 import ASSET
from route_v1 import INDEXES
from route_v1 import INDEX
from exception_detail import ASSET_ALREADY_EXISTS
from exception_detail import ASSET_NOT_FOUND
from exception_detail import INDEX_ALREADY_EXISTS
from exception_detail import INDEX_NOT_FOUND

from test.asset_api.logic.test_index import reset_indexes
from test.asset_api.logic.test_asset import reset_assets


client = TestClient(app)


def test_hello_world():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'Hello': 'World'}


def test_hello_world_wrong():
    response = client.get('/wrong_hello_world')
    assert response.status_code == 404


# Assets
test_assets = []


def test_create_asset_ok(reset_assets):
    asset = {
        'name': 'CDB Bari',
        'ir': 0.15,
        'fix_interest': 0.05,
        'duration': 1,
        'id_index': 2,
    }
    to_create_asset = asset | {'id': 0}
    response = client.post(f'/{ASSETS}', json=asset)
    test_assets.append(to_create_asset)

    assert response.status_code == 200
    assert response.json() == to_create_asset


def test_create_asset_with_wrong_json():
    asset = {
        'name': 'CDB Bari',
        'ir': 0.15,
        'fix_interest': 'wrong_fix_interest',
        'duration': 'wrong_duration',
        'id_index': 2,
    }
    response = client.post(f'/{ASSETS}', json=asset)
    assert response.status_code == 422


def test_create_asset_duplicated():
    asset = {
        'name': 'CDB Inter',  # Difference from the first.
        'ir': 0.15,
        'fix_interest': 0.05,
        'duration': 1,
        'id_index': 2,
    }
    to_create_asset = asset | {'id': 1}
    response = client.post(f'/{ASSETS}', json=asset)
    assert response.status_code == 200
    assert response.json() == to_create_asset
    test_assets.append(to_create_asset)

    response = client.post(f'/{ASSETS}', json=asset)
    assert response.status_code == ASSET_ALREADY_EXISTS.status_code
    assert response.json()['detail'] == ASSET_ALREADY_EXISTS.detail


def test_get_assets():
    response = client.get(f'/{ASSETS}')
    assert response.status_code == 200
    assert response.json() == test_assets


def test_get_asset():
    asset = test_assets[0]
    response = client.get(f"/{ASSET}/{asset['id']}")
    assert response.status_code == 200
    assert response.json() == asset


def test_get_asset_not_int_id():
    response = client.get(f'/{ASSET}/wrong_id')
    assert response.status_code == 422


def test_get_asset_non_existing_id():
    response = client.get(f'/{ASSET}/123456')
    assert response.status_code == ASSET_NOT_FOUND.status_code
    assert response.json()['detail'] == ASSET_NOT_FOUND.detail


# Indexes
test_indexes = []


def test_create_index_ok(reset_indexes):
    index = {'name': 'Test Index Name', 'value': 0.1}
    to_create_index = index | {'id': 0}
    response = client.post(f'/{INDEXES}', json=index)
    test_indexes.append(to_create_index)

    assert response.status_code == 200
    assert response.json() == to_create_index


def test_create_index_with_wrong_json():
    index = {'name': 'Test Index Name', 'value': 'wrong_value_type'}
    response = client.post(f'/{INDEXES}', json=index)
    assert response.status_code == 422


def test_create_index_duplicated():
    index = {'name': 'New Index Name', 'value': 0.2}
    to_create_index = index | {'id': 1}
    response = client.post(f'/{INDEXES}', json=index)
    assert response.status_code == 200
    assert response.json() == to_create_index
    test_indexes.append(to_create_index)

    response = client.post(f'/{INDEXES}', json=index)
    assert response.status_code == INDEX_ALREADY_EXISTS.status_code
    assert response.json()['detail'] == INDEX_ALREADY_EXISTS.detail


def test_get_indexes():
    response = client.get(f'/{INDEXES}')
    assert response.status_code == 200
    assert response.json() == test_indexes


def test_get_index():
    index = test_indexes[0]
    response = client.get(f"/{INDEX}/{index['id']}")
    assert response.status_code == 200
    assert response.json() == index


def test_get_index_not_int_id():
    response = client.get(f'/{INDEX}/wrong_id')
    assert response.status_code == 422


def test_get_index_non_existing_id():
    response = client.get(f'/{INDEX}/123456')
    assert response.status_code == INDEX_NOT_FOUND.status_code
    assert response.json()['detail'] == INDEX_NOT_FOUND.detail
