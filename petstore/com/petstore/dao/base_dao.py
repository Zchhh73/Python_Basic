'''Dao基类，基本功能的封装'''

import pymysql
import configparser
import os


class BaseDao(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(os.path.abspath(os.path.join(os.getcwd(), "../../..")),'config.ini'), encoding = 'utf-8')

        host = self.config['db']['host']
        user = self.config['db']['user']
        port = self.config.getint('db', 'port')
        password = self.config['db']['password']
        database = self.config['db']['database']
        charset = self.config['db']['charset']

        self.conn = pymysql.connect(host=host,
                                    user=user,
                                    port=port,
                                    password=password,
                                    database=database,
                                    charset=charset)

    def close(self):
        self.conn.close()
