import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class EncontrarElemento(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path='./chromedriver')
        driver=cls.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
    def test_find_textfield(self):
        driver=self.driver
        campo_texto=driver.find_element_by_id("search")
    def test_search_button_enabled(self):
        button=self.driver.find_element_by_class_name("button")
    def test_count_banner_images(self):
        banner_list=self.driver.find_element_by_class_name("promos")
        banners= banner_list.find_element_by_tag_name('img')
        print('>>>>>>>', type(banners))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='reporte-elementos'))