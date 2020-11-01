class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    ENV = "dev"
    SQLALCHEMY_DATABASE_URI = "sqlite:///starwar.db"
    SECRET_KEY = "a9eec0e0-23b7-4788-9a92-318347b9a39f"


config = {
    "dev": "starwar.config.DevelopmentConfig",
    "default": "starwar.config.DevelopmentConfig",
}


def configure_app(app):
    config_name = "default"
    app.config.from_object(config[config_name])