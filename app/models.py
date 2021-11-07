import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mugera:Mugbwo9856@localhost/pitches'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
class ProdConfig(Config):
     SQLALCHEMY_DATABASE_URI ="postgresql://anszgkllpxanst:c9d40243a350ba5207e102a94b12ed27bc3f3b5daf8e1e6a1b92d5b50d0e2738@ec2-18-206-20-102.compute-1.amazonaws.com:5432/danjuvprph6nlk?sslmode=require"

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://mugera:Mugbwo9856@localhost/pitches_tests'
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://mugera:Mugbwo9856@localhost/pitches'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
