
import unittest
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pymongo

HOST = "https://front"

def prepare_db():
    db_host = '127.0.0.1'
    client = pymongo.MongoClient(db_host, 27017)
    db = client.get_database('blog')
    db.Master.update( {'_id':'testuser'} ,{'$set':{'pw':'hoge'}}, True)

class BrowserTests(unittest.TestCase):
    def setUp(self):
        # insert a doc to DB
        #prepare_db()

        # connect to selenium
        self.driver = webdriver.Remote(
            command_executor = 'http://127.0.0.1:4444/wd/hub',
            desired_capabilities = DesiredCapabilities.CHROME
        )

        # set timeout
        self.driver.implicitly_wait(10)

    def test_top(self):
        """top page"""
        pass
        self.driver.get(HOST + "/")
        self.assertIn("Home Page", self.driver.title)

def suite():
    """run tests"""
    suite = unittest.TestSuite()
    suite.addTests([
        unittest.makeSuite(BrowserTests),
    ])
    return suite


if __name__ == '__main__':
    unittest.main()