import pytest

from fixtures.pulse_api_client import PulseAPI

@pytest.fixture(scope="session")
def app_b():
    return PulseAPI(resource="books")

@pytest.fixture(scope="session")
def app_r():
    return PulseAPI(resource="roles")

@pytest.fixture(scope="session")
def app_r(app_b):
    pass
