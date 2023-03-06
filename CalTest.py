import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class CalculatorTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://qa.errigal.com/qality/calculator?id=fmasombo")

    def test_addition(self):
        input_field = self.driver.find_element("id", "key-3")
        input_field.send_keys("3")

        add_button = self.driver.find_element("id", "sign-plus")
        add_button.click()

        input_field.send_keys("5")

        equals_button = self.driver.find_element("id", "key-5")
        equals_button.click()
        result = self.driver.find_element("id", "output")
        self.assertEqual(result.get_attribute("value"), "8")

    def test_subtraction(self):
        input_field = self.driver.find_element_by_id("input_field")
        input_field.send_keys("7")
        subtract_button = self.driver.find_element_by_id("subtract_button")
        subtract_button.click()
        input_field.send_keys("4")
        equals_button = self.driver.find_element_by_id("equals_button")
        equals_button.click()
        result = self.driver.find_element_by_id("result")
        self.assertEqual(result.get_attribute("value"), "3")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
