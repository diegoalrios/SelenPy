import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class AssertionTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        self.driver.get('http://demo-store.seleniumacademy.com/')
        self.driver.maximize_window()

    def test_search_field(self):
       self.assertTrue(self.is_elemet_present(By.NAME, 'q'))
    def test_language_option(self):
       self.assertTrue(self.is_elemet_present(By.ID, 'select-language'))

    def tearDown(self):
        self.driver.quit()

    def is_elemet_present(self,tipo_selector,valor_selector):
        try:
            self.driver.find_element(by=tipo_selector,value=valor_selector)
        except NoSuchElementException as valor:
            return False
        return True

