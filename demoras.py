##INVESTIGAR SOBRE WEBDRIVER WAIT PORQUE NO ME FUNCIONO
##INVESTIGAR SOBRE WEBDRIVER WAIT PORQUE NO ME FUNCIONO
##INVESTIGAR SOBRE WEBDRIVER WAIT PORQUE NO ME FUNCIONO
##INVESTIGAR SOBRE WEBDRIVER WAIT PORQUE NO ME FUNCIONO
##INVESTIGAR SOBRE WEBDRIVER WAIT PORQUE NO ME FUNCIONO
##INVESTIGAR SOBRE WEBDRIVER WAIT PORQUE NO ME FUNCIONO
##INVESTIGAR SOBRE WEBDRIVER WAIT PORQUE NO ME FUNCIONO  https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html DOCUMENTACION

import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By ##acceder a elementos de la Web a travez de sus selectores
from selenium.webdriver.support.ui import WebDriverWait ## hace uso de condiciones esperadas y demoras explicitas
from selenium.webdriver.support import expected_conditions ## demoras
class ExplicitWaitTest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path='./chromedriver')
        driver=self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
    def test_account_link(self):
       driver=self.driver
       WebDriverWait(self.driver,10)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='reporte_auto-navigate'))