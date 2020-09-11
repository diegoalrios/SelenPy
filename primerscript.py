import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class Pagina(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver=cls.driver
        driver.implicitly_wait(10)
    def test_holamundo(self):
        driver=self.driver
        driver.get('https://www.platzi.com')
    def test_google(self):
        self.driver.get('https://www.google.com')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='reporte-holamundo'))