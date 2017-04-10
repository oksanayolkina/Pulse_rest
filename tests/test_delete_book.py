import pytest
from models.book import Book

@pytest.fixture
def book(app_b):
    b = Book(title="QA_delete", author="Oksana_delete")
    app_b.create_object(b)
    return b

def test_delete(app_b, book):
    response = app_b.delete_object(book)
    # Verification
    assert response.status_code == 204
    # assert response.json() not in response.get_objects()