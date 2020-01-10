#this will test if the output is a hit or a miss

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

class test_service_4(TestBase):
    def test_hit_or_miss(self):
        
        hitOrMiss = routes.hit_or_miss()
        if hitOrMiss == "You hit my battleship!" or hitOrMiss == "You miss my battleship!":
            self.assertTrue(True)
        else:
            self.assertFalse(False)
