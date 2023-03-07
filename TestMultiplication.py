import unittest
from selenium import webdriver
import time


class MyTestCase(unittest.TestCase):
    # This will test the multiplication function
    def setUp(self):
        # This is using chrome
        self.driver = webdriver.Chrome()
        # Open the application using the url
        self.driver.get("http://qa.errigal.com/qality/calculator?id=fmasombo")

    def test_multiplication(self):
        # Type in the numbers from the app using the id 6x2
        self.driver.find_element("id", "key-6").click()
        self.driver.find_element("id", "sign-multiply").click()
        self.driver.find_element("id", "key-2").click()
        self.driver.find_element("id", "sign-equal").click()

        # Wait for the function to be performed
        time.sleep(4)
        result = self.driver.find_element("id", "output").get_attribute("value")

        # Assert function result 6x2 should be 12
        self.assertEqual("12.0", result)

    def test_multiplication_dd(self):
        # Type in the numbers from the app using the id 6x2
        self.driver.find_element("id", "key-6").click()
        self.driver.find_element("id", "key-6").click()
        self.driver.find_element("id", "sign-multiply").click()
        self.driver.find_element("id", "key-2").click()
        self.driver.find_element("id", "key-2").click()
        self.driver.find_element("id", "sign-equal").click()

        # Wait for the function to be performed
        time.sleep(4)
        result = self.driver.find_element("id", "output").get_attribute("value")

        # Assert function result 6x2 should be 12
        self.assertEqual("1452.0", result)

    # Finish browser instance
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
