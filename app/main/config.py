import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dd95a3e2-5219-11e9-a91b-00271064d1fc')
    DEBUG = False
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD') or '1con'
    ADMIN_EMAIL = os.environ.get(
        'ADMIN_EMAIL') or 'iroshbrian@gmail.com'


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'main.db')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jina:jinakubwa@localhost/apiV1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.sendgrid.net'
    MAIL_PORT = 587
    MAIL_USERNAME = 'apikey'
    MAIL_PASSWORD = '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'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    OCP_APIM_SUBSCRIPTION_KEY = '0f4e27be90ec4437be6960e1e2565ebd'


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jina:jinakubwa@localhost/testAPI'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
