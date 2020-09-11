import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path='./chromedriver')
        driver=cls.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()## da click en account
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[5]/div/ul/li[6]/a').click()## da click en log in

        create_account_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span')## este es el boton de crear cuenta
        self.assertTrue(create_account_button.is_enabled() and create_account_button.is_displayed())## verifica que el boton este en pantallla y abilitado
        create_account_button.click()##click en el boton create account

        ##verificar que estoy en la pagina correcta
        self.assertEqual('Create New Customer Account', driver.title)
        first_name_text_area = driver.find_element_by_id('firstname')
        middle_name_text_area = driver.find_element_by_id('middlename')
        last_name_text_area = driver.find_element_by_id('lastname')
        mail_text_area = driver.find_element_by_id('email_address')
        pss_text_area = driver.find_element_by_id('password')
        conf_pss_text_area = driver.find_element_by_id('confirmation')
        register_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button')

        ##Verifiicar que cada text area esta abilitado
        self.assertTrue(first_name_text_area.is_enabled()
            and middle_name_text_area.is_enabled()
            and last_name_text_area.is_enabled()
            and mail_text_area.is_enabled()
            and pss_text_area.is_enabled()
            and conf_pss_text_area.is_enabled()
            and register_button.is_enabled())

        ##ENVIAR DATOS A CADA UNA DE LOS TEXT AREAS
        first_name_text_area.send_keys('el')
        middle_name_text_area.send_keys('tino')
        last_name_text_area.send_keys('aspilla')
        mail_text_area.send_keys('elvergalarga@gmail.com')
        aux='12345678'
        pss_text_area.send_keys(aux)
        conf_pss_text_area.send_keys(aux)
        register_button.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='reporte_register-new-account'))