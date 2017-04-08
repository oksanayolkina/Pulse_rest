import pytest

from fixtures.pulse_api_client import PulseAPI


@pytest.fixture
def app():
    return PulseAPI(resource="books")