import pytest
from app import create_app
from config import Config


class TestConfig(Config):
    TESTING = True
    API_KEY = 'test-api-key'
    REDIS_URL = 'redis://'


@pytest.fixture
def test_app():
    test_app = create_app(TestConfig)

    yield test_app


@pytest.fixture
def test_client(test_app):
    return test_app.test_client()


@pytest.fixture
def test_runner(test_app):
    return test_app.test_cli_runner()
