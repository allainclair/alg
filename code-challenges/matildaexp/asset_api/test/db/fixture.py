from pytest import fixture

from test.db.db_create import create as c
from test.db.db_delete import delete as d


@fixture
def create():
    return c


@fixture
def delete():
    return d
