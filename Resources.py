import time
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

global driver

def start_server():
    os.system("start /B start cmd.exe @cmd /k appium")
    time.sleep(5)
def logout(driver):
    time.sleep(5)
    permission_buttons(driver)
    # time.sleep(2)
    # driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()

    time.sleep(10)
    driver.press_keycode(4)
    time.sleep(2)

    driver.start_activity("com.veristerminal", ".MainActivity")
    time.sleep(10)
    # (new TouchAction(driver)).tap(385, 676).perform()
    login(driver)
    time.sleep(10)
    driver.find_element_by_accessibility_id('settingsButton').click()
    time.sleep(3)
    driver.find_element_by_accessibility_id('Authorization Code').send_keys("1")
    time.sleep(1)
    driver.hide_keyboard()
    time.sleep(2)
    driver.find_element_by_accessibility_id('settings').click()
    time.sleep(2)
    driver.find_element_by_accessibility_id('//android.view.ViewGroup[@content-desc="logOutTerminal"]/android.view.ViewGroup').click()
    time.sleep(2)
    driver.find_element_by_id('android:id/button1').click()
    time.sleep(2)
def settingup():

    desired_capabilities = {

        "app": "C:\\Users\\veris\\Downloads\\updated_release\\Terminal-Plus-release (3).apk",
        "platformName": "Android",
        "deviceName": "fc378d12",
        "appActivity": ".MainActivity",
        "appPackage": "com.veristerminal",
        "unicodeKeyboard": False,
        " resetKeyboard": False,
        "platformVersion": "8.1",
        "appiumVersion": "1.12.1"
    }
    return desired_capabilities
def login(driver):
    element_id = driver.find_element_by_accessibility_id("Authorization ID")

    status = element_id.is_displayed()
    status = element_id.is_displayed()
    print(status)
    driver.set_value(element_id, "N1")

    driver.execute_script('mobile:performEditorAction', {'action': 'done'})
    time.sleep(2)
    element_code = driver.find_element_by_accessibility_id("Authorization Code")
    driver.set_value(element_code, "1")

    driver.execute_script('mobile:performEditorAction', {'action': 'done'})
    time.sleep(2)
    driver.find_element_by_accessibility_id("loginButton").click()
    time.sleep(20)

def checkIn(driver):
    driver.find_element_by_accessibility_id('Check-In').click()

def activity_complete(driver):
    driver.find_element_by_accessibility_id('activityCompletedButton').click()

def setting_contact(driver):

    driver.find_element_by_accessibility_id('enterMobileNumber').click()
    driver.find_element_by_accessibility_id("7").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("6").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("9").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("3").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("2").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("5").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("4").click()
    time.sleep(5)
    driver.find_element_by_accessibility_id("3").click()
    time.sleep(5)
    driver.find_element_by_accessibility_id("3").click()
    time.sleep(5)
    driver.find_element_by_accessibility_id("9").click()
    time.sleep(5)

    driver.find_element_by_accessibility_id("checkmark").click()

def permission_buttons(driver):
    for i in range(2):
        driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        time.sleep(2)
def launch_application(desired_capabilities):
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
    return driver
def NDA_screen(driver):
    #driver.find_element_by_accessibility_id('signatureField')
    driver.find_elements_by_xpath('//android.view.ViewGroup[@content-desc="signatureField"]/android.widget.LinearLayout/android.view.View')
    time.sleep(5)
    user_action=TouchAction(driver)
    user_action.press(x=166,y=978).move_to(x=377,y=915).release()
    time.sleep(5)
    user_action.tap(x=377, y=1223).perform()
    time.sleep(2)

def GOVT_Id_Screen(driver):
    driver.find_element_by_accessibility_id("cardScanClickImageButton").click()
    time.sleep(10)
    driver.find_element_by_accessibility_id("cardScanNextButton").click()
    time.sleep(5)

def FLEP_Screen(driver):
    driver.find_element_by_accessibility_id('First Name').send_keys('Test1')
    time.sleep(2)
    driver.find_element_by_accessibility_id('Last Name').send_keys('test_sur1')
    time.sleep(2)
    driver.find_element_by_accessibility_id('Email').send_keys('test@test.com')
    time.sleep(2)

    driver.execute_script('mobile:performEditorAction', {'action': 'done'})
    time.sleep(2)
    contact_element=driver.find_element_by_accessibility_id('Phone Number')
    status=contact_element.is_displayed()
    print(status)
    num=contact_element.get_attribute('text')
    print(num)
    time.sleep(3)
    driver.find_element_by_accessibility_id('nextButton').click()
    time.sleep(2)

def camera(driver):
    driver.find_element_by_accessibility_id("clickImageButton").click()
    time.sleep(10)
    driver.find_element_by_accessibility_id("nextButton").click()
    time.sleep(10)

def cardScanning(driver):
    driver.find_element_by_accessibility_id('cardScanClickImageButton').click()
    time.sleep(7)
    driver.find_element_by_accessibility_id('cardScanNextButton').click()
    time.sleep(3)

def kill_server(driver):
    driver.execute_script('mobile: shell', {
        'command': 'echo',
        'args': ['arg1', 'arg2'],
        'includeStderr': True,
        'timeout': 5000
    })
    print("server_killed")