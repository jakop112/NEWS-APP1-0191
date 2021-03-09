class BaseConfig:
    INDEX_TEMPLATE = 'index.html'
    DEBUG = False
    TESTING = False
    DB_SERVER = '192.168.1.56'
    DATABASE_URI = 'sqlite:///:memory:'

class DevConfig(BaseConfig):
    DB_SERVER = 'localhost'
    INDEX_TEMPLATE = 'dev.html'

class ProdConfig(BaseConfig):
    DEBUG = True
    DB_SERVER = '192.168.19.32'

class TestConfig(BaseConfig):
    DEBUG = True
    DB_SERVER = 'localhost'


configurations = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig,
}
