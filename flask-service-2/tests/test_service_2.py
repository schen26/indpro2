#this file will test if service 2 gives out the letters 'a' to 'e' 

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

    def setUp(self):
        pass

    def tearDown(self):
        pass

class test_service_2(TestBase):
    
    
    def test_randLet(self):
        randomLetter = routes.randLet()
        if randomLetter == 'a' or randomLetter == 'b' or randomLetter == 'c' or randomLetter == 'd' or randomLetter == 'e':
            self.assertTrue(True)
        else:
            self.assertFalse(False)

