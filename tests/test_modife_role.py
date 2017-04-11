import pytest
from models.role import Role

@pytest.fixture
def role(app_r):
    r = Role(name="QA_m", type="Oksana_m", level=10, book=1)
    app_r.create_object(r)
    return r

def test_modife(app_r, role):
    role_new = Role(id=role.id, name="QA_modife", type="Oksana_modife", level=8, book=2)
    response = app_r.modife_object(role_new)
    # Verification
    assert response.status_code == 200
    assert response.json() == role_new.get_dict_with_id()

    response = app_r.get_object(role).json()
    # Verification
    assert response["level"] == 8
    assert response["book"] == 2

    app_r.delete_object(role_new)
    app_r.delete_object(role)


def test_modife_empty_title(app_r, role):
    role_new = Role(id=role.id, name="", type="Oksana_modife")
    response = app_r.modife_object(role_new)
    # Verification
    assert response.status_code == 400

    app_r.delete_object(role)

def test_modife_empty_author(app_r, role):
    role_new = Role(id=role.id, name="QA_modife", type="")
    response = app_r.modife_object(role_new)
    # Verification
    assert response.status_code == 400

    app_r.delete_object(role)

def test_modife_empty(app_r, role):
    role_new = Role(id=role.id, name="", type="")
    response = app_r.modife_object(role_new)
    # Verification
    assert response.status_code == 400

    app_r.delete_object(role)
