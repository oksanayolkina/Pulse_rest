import pytest
from models.book import Book

@pytest.fixture
def book(app):
    b = Book(title="QA_delete", author="Oksana_delete")
    app.create_object(b)
    return b

def test_delete(app, book):
    response = app.delete_object(book)
    assert response.status_code == 204