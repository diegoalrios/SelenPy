import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
class NavigationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path='./chromedriver')
        driver=cls.driver
        driver.get('https://www.google.com/')
        driver.maximize_window()
    def test_browser_navigation(self):
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('Platzi')
        search_field.submit()

        self.driver.back()##regresar
        self.driver.forward()##adelantar
        self.driver.refresh()##actualizar
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='reporte_auto-navigate'))