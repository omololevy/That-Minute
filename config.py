import os

# rest of connection code using the connection string `uri`

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://levy:123456@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitches'
    SENDER_EMAIL = 'cotechlevy@gmail.com'
    SQLALCHEMY_DATABASE_URI ='postgresql://xielebopymckhq:fb19c8910c24d0977b0e0dfa3249b84a17b80112455b3bd81b0076ee4d54e885@ec2-34-224-239-147.compute-1.amazonaws.com:5432/dmbdlb14h4fjc'
    
# simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    @staticmethod
    def init_app(app):
        pass
    
class ProdConfig(Config):
     SQLALCHEMY_DATABASE_URI = 'postgresql://xielebopymckhq:fb19c8910c24d0977b0e0dfa3249b84a17b80112455b3bd81b0076ee4d54e885@ec2-34-224-239-147.compute-1.amazonaws.com:5432/dmbdlb14h4fjc'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://levy:123456@localhost/pitches_tests'
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://levy:123456@localhost/pitches'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
