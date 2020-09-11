import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class LanguageOptions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path='./chromedriver')
        driver=cls.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
    def test_select_language(self):
        language_options=['English','French','German']
        list_language_optioons=[]

        languages = Select(self.driver.find_element_by_id('select-language'))
        self.assertEqual(3, len(languages.options))

        for language in languages.options:
            list_language_optioons.append(language.text)

        self.assertListEqual(language_options , list_language_optioons)
        self.assertEqual('English' , languages.first_selected_option.text)##COMPRUEBA QUE EL IDIOMA POR DEFECTO SEA INGLES
        languages.select_by_index(1)##CAMBIA EL IDIONA A FRANCES

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='reporte-select-language'))