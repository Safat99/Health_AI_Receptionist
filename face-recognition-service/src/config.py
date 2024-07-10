import os

class Config:
    DEBUG = False
    
class DevelopmentConfig(Config):
    pass

class ProductionConfig(Config):
    pass


config_by_name = dict(
    dev = DevelopmentConfig,
    prod = ProductionConfig
)