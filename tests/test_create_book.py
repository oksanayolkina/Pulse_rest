import pytest
from models.book import Book

test_data = [
    Book(title="QA", author="Oksana"),
    Book(title="1", author="1"),
]

@pytest.mark.parametrize("book", test_data, ids=[repr(b) for b in test_data])
def test_create_book(app, book):
    response = app.create_object(book)
    # Verification
    assert response.status_code == 201
    assert response.json() == book.get_dict_with_id()

def test_create_book_no_author(app):
    book = Book(title="QA")
    response = app.create_object(book)
    # Verification
    assert response.status_code == 400


