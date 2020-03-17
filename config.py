# coding:utf-8
import redis

class Config(object):
    """配置信息"""
    DEBUG = True

    SECRET_KEY = "XHSOI*Y9ds9cshd9"

    #数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@localhost:3306/aijia"
    SQLALCHMY_TRACK_MODIFIONS = True

    # redis
    REDIS_HOST="127.0.0.1"
    REDIS_PORT=6379

    #flask-session配置
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.StrictRedis(host=REDIS_PORT,port=REDIS_PORT)
    SESSION_USE_SIGNER = True #对cookie中session


class DevelopmenConfig(Config):
    """开发模式的配置信息"""
    pass

class ProductionConfig(Config):
    """生产环境的配置信息"""
    pass

config_map = {
    "develop":DevelopmenConfig,
    "product":ProductionConfig
}