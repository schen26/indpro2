#this file will test if service 3 gives out the string '1' to '5' 
  
import unittest
from flask_testing import TestCase
from application import app
from os import getenv
from application import routes

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+str(getenv('MYSQL_USER'))+':'+str(getenv('MYSQL_PASS'))+'@'+str(getenv('MYSQL_URL'))+'/'+str(getenv('MYSQL_DB_TEST')))
        return app

class test_service_3(TestBase):
    def test_randNumA(self):
        randomNumber = routes.randNumA()
        if randomNumber == '1' or randomNumber == '2' or randomNumber == '3' or randomNumber == '4' or randomNumber == '5':
            self.assertTrue(True)
        else:
            self.assertFalse(False)
