import pytest
from models.role import Role

test_data = [
    Role(name="QA", type="Oksana", level=10, book=1),
    Role(name="1", type="1", level=1, book=2)
    ]

@pytest.mark.parametrize("role", test_data, ids=[repr(b) for b in test_data])
def test_create_role(app_r, role):
    response = app_r.create_object(role)
    # Verification
    assert response.status_code == 201
    assert response.json() == role.get_dict_with_id()

    app_r.delete_object(role)

def test_create_role_no_level_and_book(app_r):
    role = Role(name="QA", type="Oksana")
    response = app_r.create_object(role)
    # Verification
    assert response.status_code == 201
    assert role.get_level() is None
    assert role.get_book() is None

    app_r.delete_object(role)

def test_create_role_no_name(app_r):
    role = Role(name="Oksana")
    response = app_r.create_object(role)
    # Verification
    assert response.status_code == 400

def test_create_role_no_type(app_r):
    role = Role(type="QA")
    response = app_r.create_object(role)
    # Verification
    assert response.status_code == 400

def test_create_role_nothing(app_r):
    role = Role(name="", type="")
    response = app_r.create_object(role)
    # Verification
    assert response.status_code == 400


