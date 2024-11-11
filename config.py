import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    TESTING = False
    API_KEY = os.environ.get('SECRET_KEY') or 'fake-api-key'
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
