from app import create_app
from config import Config

class TestConfig(Config):
    TESTING = True
    API_KEY = 'test-api-key'
    REDIS_URL = 'redis://'


class RealConfig(Config):
    TESTING = False
    API_KEY = 'test-api-key'
    REDIS_URL = 'redis://'


def test_config():
    assert not create_app(RealConfig).testing
    assert create_app(TestConfig).testing
