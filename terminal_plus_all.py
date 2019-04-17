import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

global driver
def settingup():

    desired_capabilities = {

        "app": "C:\\Users\\veris\\Downloads\\terminal plus updated release\\Terminal-Plus-release (2).apk",
        "platformName": "Android",
        "deviceName": "RZ8M30B0LNZ",
        "appActivity": ".MainActivity",
        "appPackage": "com.veristerminal",
        "unicodeKeyboard": False,
        " resetKeyboard": False,
        "platformVersion": "9",
        "appiumVersion": "1.12.1"
    }
    return desired_capabilities
def login(driver):
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

def checkIn(driver):
    driver.find_element_by_accessibility_id('Check-In').click()

def activity_complete(driver):
    driver.find_element_by_accessibility_id('activityCompletedButton').click()

def setting_contact(driver):

    driver.find_element_by_accessibility_id('enterMobileNumber').click()
    driver.find_element_by_accessibility_id("9").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("1").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("9").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("9").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("9").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("5").click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("5").click()
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
    driver.find_element_by_accessibility_id('NDA').click()
    time.sleep(5)
    user_action=TouchAction(driver)
    user_action.press(x=203,y=938).move_to(x=302,y=970).release()
    time.sleep(5)
    user_action.tap(x=389, y=1223).perform()
    time.sleep(2)
def walk_in_visitor(driver):

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
    checkIn(driver)
    time.sleep(5)
    setting_contact(driver)
    time.sleep(10)
    driver.find_element_by_accessibility_id("USER_ID").click()
    time.sleep(10)

    driver.find_element_by_accessibility_id("clickImageButton").click()
    time.sleep(10)
    driver.find_element_by_accessibility_id("nextButton").click()
    time.sleep(10)
    driver.find_element_by_accessibility_id("cardScanClickImageButton").click()
    time.sleep(10)
    driver.find_element_by_accessibility_id("cardScanNextButton").click()
    time.sleep(5)

    name = driver.find_element_by_accessibility_id("Enter First namr")
    driver.set_value(name, "MANSI")
    time.sleep(5)

    driver.find_element_by_accessibility_id("nextButton").click()
    time.sleep(5)
    activity_complete(driver)
    time.sleep(5)

    user_action = TouchAction(driver)
    user_action.tap(x=450, y=906).perform()

    time.sleep(10)

    driver.find_element_by_accessibility_id('Check-Out').click()
    time.sleep(5)
    setting_contact(driver)

    time.sleep(5)
    activity_complete(driver)

    user_action = TouchAction(driver)
    user_action.tap(x=450, y=906).perform()
    time.sleep(2)
    assert True

def auto_fetch_walkin(driver):
    time.sleep(5)
    checkIn(driver)
    time.sleep(5)
    setting_contact(driver)
    time.sleep(10)
    driver.find_element_by_accessibility_id("USER_ID").click()
    time.sleep(10)

    retakeButton=driver.find_element_by_accessibility_id("retakeButton")
    status=retakeButton.is_displayed()
    print(status)
    if(status):
        print("Image autofetched test case passed")
    else:
        print("Image not autofetched test case failed")

    time.sleep(5)
    driver.find_element_by_accessibility_id("nextButton").click()
    time.sleep(10)
    retakeButton = driver.find_element_by_accessibility_id("cardScanRetakeButton")
    status_card = retakeButton.is_displayed()
    print(status_card)
    if (status_card):
        print("Image autofetched test case passed")
    else:
        print("Image not autofetched test case failed")
    time.sleep(10)
    driver.find_element_by_accessibility_id("cardScanNextButton").click()
    time.sleep(5)
    name = driver.find_element_by_accessibility_id("Enter First namr")
    status=name.is_displayed()
    myname=name.text
    print(myname)
    if(len(myname)>0):
        print("name auto fetched test case passed")

    else:
        print("test case failed")

    time.sleep(5)

    driver.find_element_by_accessibility_id("nextButton").click()
    time.sleep(5)
    activity_complete(driver)
    time.sleep(5)

    user_action = TouchAction(driver)
    user_action.tap(x=450, y=906).perform()

    time.sleep(10)

    driver.find_element_by_accessibility_id('Check-Out').click()
    time.sleep(5)
    setting_contact(driver)

    time.sleep(5)
    activity_complete(driver)

    user_action = TouchAction(driver)
    user_action.tap(x=450, y=906).perform()
    time.sleep(2)
    assert True


def main():

    desired_capabilities= settingup()
    driver=launch_application(desired_capabilities)
    walk_in_visitor(driver)
    auto_fetch_walkin(driver)

if __name__ == "__main__":
    main()