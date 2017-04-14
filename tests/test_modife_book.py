import pytest
from models.book import Book

@pytest.fixture
def book(app_b):
    b = Book(title="QA_m", author="Oksana_m")
    app_b.create_object(b)
    yield b
    app_b.delete_object(b)

def test_modife(app_b, book):
    book_new = Book(id=book.id, title="QA_modife", author="Oksana_modife")
    response = app_b.modife_object(book_new)
    # Verification
    assert response.status_code == 200
    assert response.json() == book_new.get_dict_with_id()

def test_modife_empty_title(app_b, book):
    book_new = Book(id=book.id, title="", author="Oksana_modife")
    response = app_b.modife_object(book_new)
    # Verification
    assert response.status_code == 400
    assert book_new.get_dict_with_id() not in app_b.get_objects()

def test_modife_empty_author(app_b, book):
    book_new = Book(id=book.id, title="QA_modife", author="")
    response = app_b.modife_object(book_new)
    # Verification
    assert response.status_code == 400
    assert book_new.get_dict_with_id() not in app_b.get_objects()

def test_modife_empty(app_b, book):
    book_new = Book(id=book.id, title="", author="")
    response = app_b.modife_object(book_new)
    # Verification
    assert response.status_code == 400
    assert book_new.get_dict_with_id() not in app_b.get_objects()