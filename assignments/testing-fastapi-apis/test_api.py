from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import api

client = TestClient(api.app)


@pytest.fixture(autouse=True)
def reset_books():
    api.books[:] = deepcopy(api.INITIAL_BOOKS)


def test_list_books_returns_initial_collection():
    response = client.get("/books")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_existing_book_returns_its_details():
    response = client.get("/books/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "O Jardim Secreto",
        "author": "Frances Hodgson Burnett",
        "year": 1911,
    }


# TODO: adicione os testes descritos em README.md.
