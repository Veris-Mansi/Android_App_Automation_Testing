from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AppiumTest():

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_cap={
                "app": "C:\Users\veris\Downloads\Android22\Terminal-Plus-V401-release.apk",
                "platformName": "Android",
                "deviceName": "RZ8M30B0LNZ"
            }
        )

    def tearDown(self):
        self.driver.quit()


class ExampleTests(AppiumTest):

    def test_login(self):
      assert True