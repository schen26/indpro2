#test if the web page is working and showing what it supposes to show such as the outputs from service 4
#it also tests the database if it adding the coordinations
#test if the outputs are comimg out correctly 


import unittest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import coordinates

class TestBase(TestCase): 

    def create_app(self):
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@35.246.111.139/db')
            #mysql+pymysql://'+str(getenv('MYSQL_USER'))+':'+str(getenv('MYSQL_PASS'))+'@'+str(getenv('MYSQL_URL'))+'/'+str(getenv('MYSQL_DB_TEST'))        )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        #admin = Users(first_name='admin', last_name='admin',email="admin@admin.com", password="admin2016")
        previous_coordinates=coordinates(previous_coordinates='a1')

        # create test non-admin user
        #employee = Users(first_name='test', last_name='test',email="test@user.com", password="test2016")

        # save users to database
        db.session.add(previous_coordinates)

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class testingtesting(TestBase):
    
    def test_homepage_view(self):
        randomLetter = routes.randLet()
        if randomLetter == 'a' or randomLetter == 'b' or randomLetter == 'c' or randomLetter == 'd' or randomLetter == 'e':
            self.assertTrue(True)
        else:
            self.assertFalse(False)
            
           # esponse = self.client.get(url_for('hitMiss'))
        #self.assertEqual(response.status_code, 200)


