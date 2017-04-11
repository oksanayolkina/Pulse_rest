import pytest
from models.role import Role

@pytest.fixture
def role(app_r):
    r = Role(name="QA_delete", type="Oksana_delete", level=10, book=1)
    app_r.create_object(r)
    return r

def test_delete(app_r, role):
    response = app_r.delete_object(role)
    # Verification
    assert response.status_code == 204