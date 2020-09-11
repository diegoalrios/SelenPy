import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By ##acceder a elementos de la Web a travez de sus selectores
from selenium.webdriver.support.ui import WebDriverWait ## hace uso de condiciones esperadas y demoras explicitas
from selenium.webdriver.support import expected_conditions ## demoras
class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver=self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.maximize_window()
        driver.find_element_by_xpath('/html/body/div[2]/div/ul/li[2]/a').click()
    def test_add_remove(self):
        driver = self.driver
        elements_added = 5
        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')
        for i in range(0,elements_added):
            add_button.click()
            sleep(1)
        deletes=driver.find_element_by_id('elements')
        butttons=deletes.find_elements_by_class_name('added-manually')
        print(">>>>",deletes,'\n')
        print(">>>>", type(deletes), '\n')
        print(">>>>", type(butttons), '\n')
        elements_removed = len(butttons)
        print(">>>>",elements_removed,' <<<<< PORFA FUNCIONEEEEEEEEEEEEEEEEEEEEEEEEEEEE', '\n')
        for btn in butttons:
            btn.click()
            sleep(1)
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='reporte_reto1'))