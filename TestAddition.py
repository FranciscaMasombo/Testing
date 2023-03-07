import unittest
from selenium import webdriver
import time


class TestAddition(unittest.TestCase):
    # This will test the add function
    def setUp(self):
        # This is using chrome
        self.driver = webdriver.Chrome()
        # Open the application using the url
        self.driver.get("http://qa.errigal.com/qality/calculator?id=fmasombo")

    def test_addition(self):
        # Type in the numbers from the app using the id for number 1
        self.driver.find_element("id", "key-1").click()

        # The add function with id sign-plus
        self.driver.find_element("id", "sign-plus").click()

        # Type in the numbers from the app using the id for number 3
        self.driver.find_element("id", "key-2").click()
        self.driver.find_element("id", "sign-equal").click()

        # Wait for the function to be performed
        time.sleep(4)
        result = self.driver.find_element("id", "output").get_attribute("value")

        # Assert function result
        self.assertEqual("3.0", result)

    # Finish browser instance
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
