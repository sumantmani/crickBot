import os
import logging

logger = logging.getLogger(__name__)

config = {
    'ENVIRONMENT': 'Development',
    'LOG_LEVEL': 'DEBUG',

    # 'ALLOWED_ORIGIN': 'http://localhost:9000;http://localhost:8080;https://www.yeongmang.com;https://yeongmang.com;',

    # enable authentication
    'AUTH_ON': True,

    # database part
    'DATABASE_TYPE': 'postgresql',
    'DATABASE_NAME': 'crickbet',
    'DATABASE_USER': 'targen',
    'DATABASE_PASS': 'targen',
    'DB_PORT': '5432',
    #'DB_URI': 'postgresql://yeongmang:Tarzan94@postgresqldb.cmul3fudcxfx.ap-south-1.rds.amazonaws.com:5432/api',
    'DB_URI': 'postgresql://targen:targen@localhost:5432/crickbet',

    'CREATE_KEY': '',
    'WEB_SIGN_SECRET_TOKEN': 'YHaNoq3MPEP3z',
    # tasks
    'BROKER_URL': 'redis://localhost:6379/0',
    'CACHE_URL': 'redis://localhost:6379/1',

    'HOSTNAME': '',
    'HTTP_AUTH_HEADER': 'Y_API_TOKEN',
    'HTTP_AUTH_COOKIE': 'Y_API_TOKEN',

    'API_TOKEN_MAX_AGE': 6 * 60 * 60,
    
    'BOT_TOKEN': '',

    'VERSION': '0.0.1'
}


config_locations = [
    './env.json',
]

teams = [
    'DD',
    'KXIP',
    'KKR',
    'RCB',
    'SRH',
    'CSK',
    'RR',
    'MI',


]
