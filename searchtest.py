import unittest
from selenium import webdriver

class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path='./chromedriver')
        driver=self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()

    def test_search_camisa(self):
        search_field=self.driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('pants')
        search_field.submit()

        products = self.driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li[1]/div/h2/a')
        self.assertEqual(1,len(products))

    def tearDown(self):
        self.driver.quit()