import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep

class Typos(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver=self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.maximize_window()
        driver.find_element_by_link_text('Typos').click()
    def test_find_typo(self):
        drv=self.driver
        text_to_check = drv.find_element_by_xpath('/html/body/div[2]/div/div/p[2]')
        validate_text = text_to_check.text
        correct_text = "Sometimes you'll see a typo, other times you won't."
        tries=1

        ##print(validate_text)

        while validate_text != correct_text:
            ##print("X \n")
            text_to_check = drv.find_element_by_xpath('/html/body/div[2]/div/div/p[2]')
            validate_text = text_to_check.text
            tries += 1
            drv.refresh()

        print(f"intentos {tries} >>>>>>>")

    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main(verbosity=2)