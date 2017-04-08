import pytest

from fixtures.pulse_api_client import PulseAPI

@pytest.fixture(scope="session")
def app():
    return PulseAPI(resource="books")


