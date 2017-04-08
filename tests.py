import unittest

from models import Book
from models import Role

from les5home5.pulse_api_client import PulseAPI


class BooksTests(unittest.TestCase):

    def setUp(self):
        self.app = PulseAPI("books")

    def test1_create_book(self):
        book = Book(title="QA", author="Oksana")
        response = self.app.create_object(book)
        self.__class__.book = book
        # Verification
        assert response.status_code == 201
        self.assertDictEqual(response.json(), book.get_dict_with_id())

    # def test2_test(self):
    #     book = Book(id=self.__class__.book.get_id(), title="QA", author="Oksana")
    #     response = self.app.get_objects()
    #     assert book.get_dict_with_id in response

    def test3_get_book(self):
        response = self.app.get_object(self.__class__.book)
        # Verification
        assert response.status_code == 200

    def test4_modife_book(self):
        book_new = Book(id=self.__class__.book.get_id(), title="QA_new", author="Oksana_new")
        response = self.app.modife_object(book_new)
        self.__class__.book_new = book_new
        assert response.status_code == 200

    # @unittest.skip("игнор")
    def test5_delete_book(self):
        response = self.app.delete_object(self.__class__.book)
        # Verification
        assert response.status_code == 204

class RolesTests(unittest.TestCase):

    def setUp(self):
        self.app = PulseAPI("roles")

    def test1_create_role(self):
        role = Role(name="Oksana", type="QA", level=2, book=1)
        response = self.app.create_object(role)
        self.__class__.role = role
        # Verification
        self.assertEqual(response.status_code, 201)
        self.assertDictEqual(response.json(), role.get_dict_with_id())

    def test2_get_role(self):
        response = self.app.get_object(self.__class__.role)
        # Verification
        self.assertEqual(response.status_code, 200)

    def test3_modife_role(self):
        role_new = Role(id=self.__class__.role.get_id(), name="Oksana_new", type="QA_new", level=21, book=2)
        response = self.app.create_object(role_new)
        self.__class__.role_new = role_new
        # Verification
        self.assertEqual(response.status_code, 201)

#   @unittest.skip("игнор")
    def test4_delete_role(self):
        response = self.app.delete_object(self.__class__.role)
        # Verification
        self.assertEqual(response.status_code, 204)