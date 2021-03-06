import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

desired_cap={
  "app": "C:\\Users\\veris\\Downloads\\nikhil2\\Terminal-Plus-release (1).apk",
  "platformName": "Android",
  "deviceName": "92ddcb31",
  "appActivity": ".MainActivity",
  "appPackage": "com.veristerminal",
  "unicodeKeyboard": False,
  " resetKeyboard": False
}


#We can invoke our application in real device
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

driver.implicitly_wait(20)
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()

driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
#time.sleep(2)
#WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH,'//android.view.ViewGroup[@content-desc="loginID"]')))
element=driver.find_element_by_accessibility_id("Authorization ID")

driver.set_value(element,"V")
driver.execute_script('mobile:performEditorAction',{'action':'done'})

#WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH,'//android.view.ViewGroup[@content-desc="loginCode"]')))
el = driver.find_element_by_accessibility_id("Authorization Code")

driver.set_value(el,"9")
driver.execute_script('mobile:performEditorAction',{'action':'done'})

WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH,'//android.view.ViewGroup[@content-desc="loginButton"]')))
driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="loginButton"]').click()

driver.find_element_by_accessibility_id('Check-In').click()

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

driver.find_element_by_accessibility_id("activityCompletedButton").click()