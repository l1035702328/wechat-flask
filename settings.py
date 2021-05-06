class Config(object):
    """Base config, uses staging database server."""
    DEBUG = False
    TESTING = False
    DB_SERVER = '192.168.1.56'

    @property
    def DATABASE_URI(self):         # Note: all caps
        return 'mysql://user@{}/foo'.format(self.DB_SERVER)


# 生产环境
class ProductionConfig(Config):
    DB_SERVER = '192.168.19.32'
    DEBUG = False
    RE_WATER_PATH = '/dropFile/'
    PHOTO_PATH = '/photo/'


# 开发环境
class DevelopmentConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True
    RE_WATER_PATH = 'F:\wechatmain\wechat-flask\\'
    PHOTO_PATH = '/photo/'


# 测试环境
class TestingConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True
    DATABASE_URI = 'sqlite:///:memory:'