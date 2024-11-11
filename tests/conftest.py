import pytest
from app import create_app
from config import Config


class TestConfig(Config):
    TESTING = True
    API_KEY = 'test-api-key'
    REDIS_URL = 'redis://'


@pytest.fixture
def app():
    app = create_app(TestConfig)

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
