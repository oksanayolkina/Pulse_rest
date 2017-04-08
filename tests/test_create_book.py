from models.book import Book

def test_create_book(app):
    book = Book(title="QA", author="Oksana")
    response = app.create_object(book)
    # Verification
    assert response.status_code == 201
    assert response.json() == book.get_dict_with_id()

def test_create_book_no_author(app):
    book = Book(title="QA")
    response = app.create_object(book)
    # Verification
    assert response.status_code == 400


# # def test2_test(self):
# #     book = Book(id=self.__class__.book.get_id(), title="QA", author="Oksana")
# #     response = self.app.get_objects()
# #     assert book.get_dict_with_id in response
#
# def test_3_get_book(app):
#     response = app.get_object(app.__class__.book)
#     # Verification
#     assert response.status_code == 200
#
# def test_4_modife_book(app):
#     book_new = Book(id=app.__class__.book.get_id(), title="QA_new", author="Oksana_new")
#     response = app.modife_object(book_new)
#     app.__class__.book_new = book_new
#     assert response.status_code == 200
#
# # @unittest.skip("игнор")
# def test_5_delete_book(app):
#     response = app.delete_object(app.__class__.book)
#     # Verification
#     assert response.status_code == 204

