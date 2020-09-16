import unittest
from selenium import webdriver

class Typos(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver=self.driver
        driver.get('https://www.mercadolibre.com/')
        driver.maximize_window()
        driver.find_element_by_link_text('Colombia').click()
    def test_article(self):
        drv=self.driver
        page_tittle='Mercado Libre Colombia'
        if page_tittle==drv.title:
            seach_input=drv.find_element_by_xpath('//input[@class="nav-search-input"]')
            seach_input.send_keys('')
            seach_input.send_keys('amd')
            seach_input.submit()

        else:
            self.assertEqual(page_tittle,drv.title)
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main(verbosity=2)
