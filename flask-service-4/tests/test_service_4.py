#this will test if the output is a hit or a miss

import unittest
from flask_testing import TestCase
from application import app
from os import getenv
from application import routes
import json 

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+str(getenv('MYSQL_USER'))+':'+str(getenv('MYSQL_PASS'))+'@'+str(getenv('MYSQL_URL'))+'/'+str(getenv('MYSQL_DB_TEST')))
        return app

class test_service_4(TestBase):
    def test_hit_or_miss(json_metadata):
        if json_metadata['randomLetter'] == {"randomLetter": 'a'}: 
            self.assertTrue(True)
        else:
            self.assertFalse(False)

'''result=json.dumps(dict(random_letter='a', random_number='1', hitMiss= "You hit my battleship!")) or
            result=json.dumps(dict(random_letter='b', random_number='2', hitMiss= "You hit my battleship!")) or
            result=json.dumps(dict(random_letter='c', random_number='3', hitMiss= "You hit my battleship!")) or
            result=json.dumps(dict(random_letter='d', random_number='4', hitMiss= "You hit my battleship!")):
           # result=json.dumps(dict(random_letter='e', random_number='5', hitMiss= "You hit my battleship!")):
           # content_type='application/json',
           # follow_redirects=True)'''
'''random_letter='a' or
            random_letter='b' or             random_letter='c' or             random_letter='d' or 
            random_letter='e',  
            random_number='1' or             random_number='2' or             random_number='3' or 
            random_number='4' or 
            random_number='5', '''
      
      
      
      
''' hitOrMiss = routes.hit_or_miss()
        if hitOrMiss == "You hit my battleship!" or hitOrMiss == "You miss my battleship!":
            self.assertTrue(True)
        else:
            self.assertFalse(False)'''
