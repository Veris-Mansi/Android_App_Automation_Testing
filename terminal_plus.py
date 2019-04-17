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


driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_capabilities)
time.sleep(2)
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
time.sleep(2)

driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()

time.sleep(5)
element_id =driver.find_element_by_accessibility_id("Authorization ID")
status=element_id.is_displayed()

print(status)
driver.set_value(element_id,"V")

driver.execute_script('mobile:performEditorAction',{'action':'done'})
time.sleep(5)
element_code=driver.find_element_by_accessibility_id("Authorization Code")
driver.set_value(element_code,"9")

driver.execute_script('mobile:performEditorAction',{'action':'done'})
time.sleep(5)
driver.find_element_by_accessibility_id("loginButton").click()
time.sleep(20)
driver.find_element_by_accessibility_id('Check-In').click()
time.sleep(5)
driver.find_element_by_accessibility_id('enterMobileNumber').click()
driver.find_element_by_accessibility_id("9").click()
driver.find_element_by_accessibility_id("5").click()
driver.find_element_by_accessibility_id("5").click()
driver.find_element_by_accessibility_id("7").click()
driver.find_element_by_accessibility_id("6").click()
driver.find_element_by_accessibility_id("4").click()
driver.find_element_by_accessibility_id("7").click()
driver.find_element_by_accessibility_id("4").click()
driver.find_element_by_accessibility_id("9").click()
driver.find_element_by_accessibility_id("6").click()

driver.find_element_by_accessibility_id("checkmark").click()
time.sleep(5)
driver.find_element_by_accessibility_id("USER_ID").click()
time.sleep(10)


driver.find_element_by_accessibility_id("clickImageButton").click()
time.sleep(10)
driver.find_element_by_accessibility_id("nextButton").click()
time.sleep(10)
driver.find_element_by_accessibility_id("cardScanClickImageButton").click()
time.sleep(10)

driver.find_element_by_accessibility_id("cardScanNextButton").click()
time.sleep(2)

name=driver.find_element_by_accessibility_id("Enter First namr")
driver.set_value(name,"MANSI")
driver.find_element_by_accessibility_id("nextButton").click()

next=driver.find_element_by_accessibility_id('nextButton')
next.click()
