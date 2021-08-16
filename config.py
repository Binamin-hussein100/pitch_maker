class Config:
    
    SECRET_KEY = 'hussein'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:binamin@localhost/pitches'
    @staticmethod
    def init_app(app):
        pass
class DevConfig(Config):
    pass 

class ProdConfig(Config):
    DEBUG = True
    
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}