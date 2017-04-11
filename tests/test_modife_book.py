import pytest
from models.book import Book

@pytest.fixture
def book(app_b):
    b = Book(title="QA_m", author="Oksana_m")
    app_b.create_object(b)
    return b

def test_modife(app_b, book):
    book_new = Book(id=book.id, title="QA_modife", author="Oksana_modife")
    response = app_b.modife_object(book_new)
    # Verification
    assert response.status_code == 200
    assert response.json() == book_new.get_dict_with_id()

    app_b.delete_object(book)
    app_b.delete_object(book_new)

def test_modife_empty_title(app_b, book):
    book_new = Book(id=book.id, title="", author="Oksana_modife")
    response = app_b.modife_object(book_new)
    # Verification
    assert response.status_code == 400

    app_b.delete_object(book)

def test_modife_empty_author(app_b, book):
    book_new = Book(id=book.id, title="QA_modife", author="")
    response = app_b.modife_object(book_new)
    # Verification
    assert response.status_code == 400

    app_b.delete_object(book)

def test_modife_empty(app_b, book):
    book_new = Book(id=book.id, title="", author="")
    response = app_b.modife_object(book_new)
    # Verification
    assert response.status_code == 400

    app_b.delete_object(book)