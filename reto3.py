import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By  ##acceder a elementos de la Web a travez de sus selectores
from selenium.webdriver.support.ui import WebDriverWait  ## hace uso de condiciones esperadas y demoras explicitas
from selenium.webdriver.support import expected_conditions as EC ## demoras


def abilitar(is_txt_enabled, enable_disable_button,driver):
    if (is_txt_enabled == False):
        enable_disable_button.click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > input[type=text]")))


class DynamicControls(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.maximize_window()
        driver.find_element_by_link_text('Dynamic Controls').click()

    def test_dynamic_controls(self):
        driver = self.driver
        checkbox = driver.find_element_by_css_selector('#checkbox > input[type=checkbox]')
        remove_add_button = driver.find_element_by_css_selector('#checkbox-example > button')
        checkbox.click()
        remove_add_button.click()

        WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#checkbox-example > button")))
        remove_add_button.click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkbox-example > button")))
        remove_add_button.click()

        text_area = driver.find_element_by_css_selector('#input-example > input[type=text]')
        enable_disable_button = driver.find_element_by_css_selector('#input-example > button')
        is_txt_enabled=text_area.is_enabled()
        abilitar(is_txt_enabled,enable_disable_button,driver)
        text_area.send_keys('holi')
        sleep(5)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)