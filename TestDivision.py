import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TestDivision(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://qa.errigal.com/qality/calculator?id=fmasombo")

    def test_addition(self):
        self.driver.find_element("id", "key-1").click()
        self.driver.find_element("id", "sign-plus").click()
        self.driver.find_element("id", "key-2").click()
        self.driver.find_element("id", "sign-equal").click()
        time.sleep(4)
        result = self.driver.find_element("id", "output").get_attribute("value")
        self.assertEqual("3", result)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
