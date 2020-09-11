import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class CompareProduct(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path='./chromedriver')
        driver=cls.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
    def test_remove_alert(self):
        seach_field=self.driver.find_element_by_name('q')
        seach_field.clear()
        seach_field.send_keys('tee')
        seach_field.submit()

        self.driver.find_element_by_class_name('link-compare').click()
        self.driver.find_element_by_link_text('Clear All').click()

        alert = self.driver.switch_to.alert
        self.assertEqual('Are you sure you would like to remove all products from your comparison?',alert.text)
        alert.accept()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='reporte-alertas'))