import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

desired_capabilities={

  "app": "C:\\Users\\veris\\Downloads\\terminal plus updated release\\Terminal-Plus-release (2).apk",
  "platformName": "Android",
  "deviceName": "fc378d12",
  "appActivity": ".MainActivity",
  "appPackage": "com.veristerminal",
  "unicodeKeyboard": False,
  " resetKeyboard": False,
  "platformVersion": "8.1.0",
  "appiumVersion": "1.12.1"

}

driver= webdriver.Remote("http://localhost:4723/wd/hub",desired_capabilities)
time.sleep(2)
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
time.sleep(3)
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
driver.implicitly_wait(500)

element_id = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Authorization ID"]')
driver.set_value(element_id,"V")

driver.execute_script('mobile:performEditorAction',{'action':'done'})
time.sleep(5)

element_code=driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Authorization Code"]')
driver.set_value(element_code,'9')

driver.execute_script('mobile:performEditorAction',{'action':'done'})
time.sleep(5)

driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="loginButton"]').click()
time.sleep(20)
