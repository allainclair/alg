# TODO: Create each test case isolated with _start_db correctly
# TODO: Create other tests for more complex flows. ex: create -> get -> update -> delete

from icecream import ic
from api_model.index import Index as IndexAPI
from dbmodel.index import Index

from logic.index import (
    create,
    get,
    get_all,
    delete,
    update,
    _add,
    _get_by_attributes,
    _get_by_id,
)

from db.app import (
    start as db_start,
)

from test.db.db_delete import delete as db_delete


index_0 = {'name': 'Index 0', 'value': 0.1}
index_api_0 = IndexAPI(**index_0)
index_1 = {'name': 'Index 1', 'value': 0.1}
index_api_1 = IndexAPI(**index_1)
index_2 = Index(name='Index 2', value=0.1)


def _start_db():
    db_delete()
    db_start()


def test_create_one_without_id():
    _start_db()

    created_index = create(index_2)
    assert index_2.id is None
    assert created_index.id is not None


def test_create_already_exists():
    assert not create(index_2)


def test_get_ok():
    _start_db()
    created_index = create(index_api_0)
    assert get(created_index.id) == created_index


def test_get_with_wrong_id():
    assert not get('wrong_id')


def test_get_all_empty():
    _start_db()
    assert not get_all()


def test_get_all_one():
    _start_db()

    index_api = IndexAPI(**index_0)
    index_api = _add(index_api)

    indexes = get_all()
    index_model = indexes[0]

    assert len(get_all()) == 1
    assert index_api == IndexAPI(**dict(index_model))


def test_get_all_two_or_more():
    _start_db()
    index_api_0_with_id = _add(index_api_0)
    index_api_1_with_id = _add(index_api_1)

    indexes = get_all()

    assert len(get_all()) == 2
    assert [index_api_0_with_id, index_api_1_with_id] == indexes


def test_delete():
    index_model = _get_by_attributes(index_api_0)
    deleted_index_model = delete(index_model.id)
    assert index_model == deleted_index_model


def test_delete_with_wrong_id():
    assert not delete('wrong_id')


def test_update():
    index_model = _get_by_attributes(index_api_1)
    index_api = IndexAPI(**dict(index_model))
    index_api.name = 'New index name'
    new_index_api = update(index_model.id, index_api)

    index_api.id = index_model.id
    assert new_index_api == index_api


def test_update_with_wrong_id():
    assert not update('wrong_id', index_api_0)


def test__add():
    new_index = _add(index_2)
    assert new_index.id is not None
    new_index.id = None
    assert new_index == index_2


def test__get_by_attributes():
    _start_db()
    new_index = _add(index_2)
    assert _get_by_attributes(new_index) == new_index


def test__get_by_id():
    _start_db()
    new_index = _add(index_2)
    assert _get_by_id(new_index.id) == new_index
