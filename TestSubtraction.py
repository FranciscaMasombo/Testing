import unittest
from selenium import webdriver
import time


class MyTestCase(unittest.TestCase):
    # This will test the subtraction function
    def setUp(self):
        # This is using chrome
        self.driver = webdriver.Chrome()
        # Open the application using the url
        self.driver.get("http://qa.errigal.com/qality/calculator?id=fmasombo")

    def test_subtraction(self):
        # Type in the numbers from the app using the id
        self.driver.find_element("id", "key-6").click()
        self.driver.find_element("id", "sign-minus").click()
        self.driver.find_element("id", "key-2").click()
        self.driver.find_element("id", "sign-equal").click()

        # Wait for the function to be performed
        time.sleep(4)
        result = self.driver.find_element("id", "output").get_attribute("value")

        # Assert function result 6 -2 should be equal to 4
        self.assertEqual("4.0", result)

    # Finish browser instance
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
