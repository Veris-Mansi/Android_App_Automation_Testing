import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def set_up():

    desired_capabilities = {

        "app": "C:\\Users\\veris\\Downloads\\terminal plus updated release\\Terminal-Plus-release (2).apk",
        "platformName": "Android",
        "deviceName": "fc378d12",
        "appActivity": ".MainActivity",
        "appPackage": "com.veristerminal",
        "unicodeKeyboard": False,
        " resetKeyboard": False,
        "platformVersion": "8.1",
        "appiumVersion": "1.12.1"
    }

def test_walk_in_visitor():
    set_up()
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

    for i in range(2):
        driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        time.sleep(2)

    # time.sleep(2)
    # driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()

    time.sleep(10)
    driver.press_keycode(4)
    time.sleep(2)
    driver.start_activity("com.veristerminal", ".MainActivity")
    time.sleep(10)
    # (new TouchAction(driver)).tap(385, 676).perform()

    element_id = driver.find_element_by_accessibility_id("Authorization ID")

    status = element_id.is_displayed()
    status = element_id.is_displayed()
    print(status)
    driver.set_value(element_id, "V")

    driver.execute_script('mobile:performEditorAction', {'action': 'done'})
    time.sleep(2)
    element_code = driver.find_element_by_accessibility_id("Authorization Code")
    driver.set_value(element_code, "9")

    driver.execute_script('mobile:performEditorAction', {'action': 'done'})
    time.sleep(2)
    driver.find_element_by_accessibility_id("loginButton").click()
    time.sleep(20)
    driver.find_element_by_accessibility_id('Check-In').click()
    time.sleep(10)
    driver.find_element_by_accessibility_id('enterMobileNumber').click()
    driver.find_element_by_accessibility_id("9").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("7").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("9").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("9").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("6").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("5").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("5").click()
    time.sleep(5)
    driver.find_element_by_accessibility_id("5").click()
    time.sleep(5)
    driver.find_element_by_accessibility_id("5").click()
    time.sleep(5)
    driver.find_element_by_accessibility_id("5").click()
    time.sleep(5)

    driver.find_element_by_accessibility_id("checkmark").click()
    time.sleep(10)
    driver.find_element_by_accessibility_id("USER_ID").click()
    time.sleep(10)

    driver.find_element_by_accessibility_id("clickImageButton").click()

    driver.find_element_by_accessibility_id("nextButton").click()
    time.sleep(10)
    driver.find_element_by_accessibility_id("cardScanClickImageButton").click()

    driver.find_element_by_accessibility_id("cardScanNextButton").click()
    time.sleep(2)

    name = driver.find_element_by_accessibility_id("Enter First namr")
    myname = name.get_attribute('text')
    print(myname)
    if (len(myname) > 0):
        driver.set_value(name, "MANSI")
        time.sleep(5)

    driver.find_element_by_accessibility_id("nextButton").click()
    time.sleep(5)
    driver.find_element_by_accessibility_id('activityCompletedButton').click()
    time.sleep(5)

    user_action = TouchAction(driver)
    user_action.tap(x=450, y=906).perform()

    time.sleep(10)

    driver.find_element_by_accessibility_id('Check-Out').click()
    time.sleep(5)
    driver.find_element_by_accessibility_id('enterMobileNumber').click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("9").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("7").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("9").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("9").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("6").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("5").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("5").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("5").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("5").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("5").click()
    time.sleep(2)

    driver.find_element_by_accessibility_id("nextButton").click()
    time.sleep(5)
    driver.find_element_by_accessibility_id('activityCompletedButton').click()

    user_action = TouchAction(driver)
    user_action.tap(x=450, y=906).perform()
    assert True

def teardown_module(module):
    print("All tests done")
