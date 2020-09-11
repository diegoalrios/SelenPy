import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By ##acceder a elementos de la Web a travez de sus selectores
from selenium.webdriver.support.ui import WebDriverWait ## hace uso de condiciones esperadas y demoras explicitas
from selenium.webdriver.support import expected_conditions ## demoras
class DynamicElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver=self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.maximize_window()
        driver.find_element_by_link_text('Disappearing Elements').click()
    def test_dynamic_elemnt(self):
        driver = self.driver

        list_options = []
        cont_tries = 1
        menu_options=5

        while len(list_options) < 5:
            list_options.clear()
            for i in range(menu_options):
                try:
                    option_name = driver.find_element_by_xpath(f"/html/body/div[2]/div/div/ul/li[{i+1}]/a")
                    list_options.append(option_name.text)
                    print(list_options)
                except:
                    cont_tries += 1
                    driver.refresh()
        print("tries ", cont_tries)
            
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='reporte_reto2'))