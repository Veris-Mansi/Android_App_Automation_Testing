import time
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def start_server():
    # if server is already started in some port then it will not show error and requests will be sent to that paticular server

    os.system("start /B start cmd.exe @cmd /k appium")
    time.sleep(5)

def settingup():

    desired_capabilities = {

        "app": "C:\\Users\\veris\\Downloads\\updated_release2\\Terminal-Plus-release (4).apk",
        "platformName": "Android",
        "deviceName": "a9a95ab4",
        "appActivity": ".MainActivity",
        "appPackage": "com.veristerminal",
        "unicodeKeyboard": False,
        " resetKeyboard": False,
        "platformVersion": "7.1.1",
        "appiumVersion": "1.12.1"
    }
    walkin_details = {
        "firstname": "test_one",
        "lastname": "test_surname",
        "email": "test@test.com"
    }
    member_details = {
        "firstname": "mansi",
        "lastname": "sahu",
        "email": "mansisahu1480@gmail.com",
        "phone":"9993483676"
    }
    invited_details = {
        "firstname": "test_invite ",
        "lastname": "test_invite_surname",
        "email": "",
        "phone":"3333333333"
    }

    data={}
    data['desired_capabilities']=desired_capabilities
    data['walkin_details']=walkin_details
    data['member_details']=member_details
    data['invited_details']=invited_details
    return data

def permission_buttons(driver):
    for i in range(2):
        driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        time.sleep(2)

def launch_application(desired_capabilities):
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
    return driver

def login(driver):
    time.sleep(3)
    permission_buttons(driver)

    time.sleep(10)
    """driver.press_keycode(4)
    time.sleep(2)

    driver.start_activity("com.veristerminal", ".MainActivity")
    time.sleep(10)"""

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
    time.sleep(10)
    assert True
def checkIn(driver):
    driver.find_element_by_accessibility_id('Check-In').click()

def setting_contact_invite(driver):
    driver.find_element_by_accessibility_id('enterMobileNumber').click()
    for i in range(10):
        driver.find_element_by_accessibility_id("3").click()
        time.sleep(1)

    driver.find_element_by_accessibility_id("checkmark").click()

def setting_contact(driver):

    driver.find_element_by_accessibility_id('enterMobileNumber').click()
    for i in range(5):

        driver.find_element_by_accessibility_id("2").click()
        time.sleep(1)
    for i in range(5):
        driver.find_element_by_accessibility_id("1").click()
        time.sleep(1)
    driver.find_element_by_accessibility_id("checkmark").click()
    time.sleep(1)
def setting_contact_member(driver):

    driver.find_element_by_accessibility_id('enterMobileNumber').click()
    driver.find_element_by_accessibility_id("9").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("9").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("9").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("3").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("4").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("8").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("3").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("6").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("7").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("6").click()
    time.sleep(1)

    driver.find_element_by_accessibility_id("checkmark").click()

def camera(driver):
    driver.find_element_by_accessibility_id("clickImageButton").click()
    time.sleep(10)
    driver.find_element_by_accessibility_id("nextButton").click()
    time.sleep(10)
def cameraretake(driver):
    time.sleep(2)
    retakeButton = driver.find_element_by_accessibility_id("retakeButton")
    status = retakeButton.is_displayed()
    print(status)
    if (status):
        print("Image autofetched test case passed")
    else:
        print("Image not autofetched test case failed")

    time.sleep(5)
    driver.find_element_by_accessibility_id("nextButton").click()
    time.sleep(1)

def FLEP_Screen(driver,walkin_details):
    driver.find_element_by_accessibility_id('First Name').send_keys(walkin_details['firstname'])
    time.sleep(2)
    driver.find_element_by_accessibility_id('Last Name').send_keys(walkin_details['lastname'])
    time.sleep(2)
    driver.find_element_by_accessibility_id('Email').send_keys(walkin_details['email'])
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

def FLEP_auto_fetch_member(driver,member_details):
    time.sleep(5)
    Fname = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="First Name"]/android.widget.EditText')
    status = Fname.is_displayed()
    print(status)
    text = Fname.text
    print(text)
    if (len(text) > 0 and text == member_details['firstname']):
        print("Fname autofetched test case passed")
    else:
        print("Fname autofetched test case failed")

    time.sleep(3)
    Lname = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Last Name"]/android.widget.EditText')
    status = Lname.is_displayed()
    print(status)
    text1 = Lname.text
    print(text1)
    if (len(text1) > 0 and text1 == member_details['lastname']):
        print("Lname autofetched test case passed")
    else:
        print("Lname autofetched test case failed")

    time.sleep(3)
    Email = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Email"]/android.widget.EditText')
    status = Email.is_displayed()
    print(status)
    text2 = Email.text
    print(text2)
    if (len(text) == 0):
        driver.set_value(Email,'test@invite.aacom')
        time.sleep(3)
    else:
        if (len(text2) > 0 and text2 == member_details['email']):
            print("Email autofetched test case passed")
        else:
            print("Email autofetched test case failed")

    time.sleep(3)
    Phone = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Phone Number"]/android.widget.EditText')
    status = Phone.is_displayed()
    print(status)
    text4 = Phone.text
    print(text4)
    if (len(text4) > 0 and text4 == member_details['phone']):
        print("Contact autofetched test case passed")
    else:
        print("Contact autofetched test case failed")

    time.sleep(2)
    driver.find_element_by_accessibility_id('nextButton').click()
    time.sleep(2)

def FLEP_auto_fetch_visitor(driver,visitor_details):
    time.sleep(5)
    Fname = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="First Name"]/android.widget.EditText')
    status = Fname.is_displayed()
    print(status)
    text = Fname.text
    print(text)
    if (len(text) > 0 and text == visitor_details['firstname']):
        print("Fname autofetched test case passed")
    else:
        print("Fname autofetched test case failed")

    time.sleep(3)
    Lname = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Last Name"]/android.widget.EditText')
    status = Lname.is_displayed()
    print(status)
    text1 = Lname.text
    print(text1)
    if (len(text1) > 0 and text1 == visitor_details['lastname']):
        print("Lname autofetched test case passed")
    else:
        print("Lname autofetched test case failed")

    time.sleep(3)
    Email = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Email"]/android.widget.EditText')
    status = Email.is_displayed()
    print(status)
    text2 = Email.text
    print(text2)
    print(len(text2))
    if(text2 == 'Email'):
        driver.set_value(Email,'testinvite@a.nn')
    else:
        if (len(text2) > 0 and text2 == visitor_details['email']):
            print("Email autofetched test case passed")
        else:
            print("Email autofetched test case failed")

    time.sleep(3)
    Phone = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Phone Number"]/android.widget.EditText')
    status = Phone.is_displayed()
    print(status)
    text4 = Phone.text
    print(text4)
    if (len(text4) > 0 and Phone == visitor_details['phone']):
        print("Contact autofetched test case passed")
    else:
        print("Contact autofetched test case failed")

    time.sleep(2)
    driver.find_element_by_accessibility_id('nextButton').click()
    time.sleep(2)

def Meeting_with_screen(driver):

    meeting = driver.find_element_by_accessibility_id('Whom To Meet')
    driver.set_value(meeting, "man")
    time.sleep(3)
    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]').click()
    driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="losmansi sahu"]/android.view.ViewGroup/android.widget.TextView[1]').click()
    #driver.find_element_by_xpath('	//android.view.ViewGroup[@content-desc="losmansi sahu"]/android.view.ViewGroup')
    #driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="losmansi sahu"]').click()
    time.sleep(2)
    driver.hide_keyboard()
    time.sleep(1)

def unique_id(driver):
    time.sleep(2)
    id =driver.find_element_by_accessibility_id('Unique_id')
    driver.set_value(id,'test111')
    time.sleep(2)

def gender_Screen(driver):
    time.sleep(2)
    gender = []
    gender = driver.find_elements_by_xpath(
        '//android.view.ViewGroup[@content-desc="radioButtonField"]/android.view.ViewGroup/android.view.ViewGroup')
    print(len(gender))
    status_radio = gender[0].is_selected()
    print(status_radio)
    if (status_radio == False):
        gender[0].click()
    time.sleep(1)

def Multi_select_screen(driver):
    driver.find_element_by_accessibility_id('dropdownFormComponentField').click()
    time.sleep(3)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button').click()
    time.sleep(1)
    driver.find_element_by_accessibility_id('nextButton').click()
    time.sleep(3)
def single_dropdown_screen(driver):

    driver.find_element_by_accessibility_id('dropdownFormComponentField').click()
    time.sleep(5)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
    # user_action.tap(x=400,y=203).release().perform()
    time.sleep(2)
    #user_action = TouchAction(driver)
    #user_action.tap(x=403, y=1211).release().perform()
    # driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button').click()
    # user_action.perform(x=400,y=1211).release().perform()
    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button').click()
    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button')
    time.sleep(2)

def cardScanning(driver):
    driver.find_element_by_accessibility_id('cardScanClickImageButton').click()
    time.sleep(7)
    driver.find_element_by_accessibility_id('cardScanNextButton').click()
    time.sleep(3)
def rating_Screen(driver):
    time.sleep(2)
    listss = driver.find_elements_by_xpath(
        '//android.view.ViewGroup[@content-desc="ratingField"]/android.widget.Button')
    print(len(listss))
    listss[3].click()
    time.sleep(1)

def emergency_contact(driver):

    driver.find_element_by_accessibility_id('Emergency contact name').send_keys('TOM')
    driver.execute_script('mobile:performEditorAction', {'action': 'done'})
    time.sleep(1)
    driver.find_element_by_accessibility_id('Emergency contact').send_keys('9988776655')
    driver.execute_script('mobile:performEditorAction', {'action': 'done'})
    time.sleep(1)

def NDA_screen(driver):
    #driver.find_element_by_accessibility_id('signatureField')
    driver.find_elements_by_xpath('//android.view.ViewGroup[@content-desc="signatureField"]/android.widget.LinearLayout/android.view.View')
    time.sleep(1)
    user_action=TouchAction(driver)
    user_action.press(x=240,y=791).move_to(x=369,y=739).release()
    time.sleep(5)
    user_action.tap(x=375, y=989).perform()
    time.sleep(2)
def date_and_time(driver):
    time.sleep(2)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup').click()
    time.sleep(2)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]').click()

    time.sleep(3)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup').click()
    time.sleep(2)
    driver.find_element_by_id('android:id/button1').click()
    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TimePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]').click()
    time.sleep(1)
    driver.find_element_by_accessibility_id('nextButton').click()
    time.sleep(2)
def GOVT_Id_Screen(driver):
    driver.find_element_by_accessibility_id("cardScanClickImageButton").click()
    time.sleep(10)
    driver.find_element_by_accessibility_id("cardScanNextButton").click()
    time.sleep(5)
def activity_complete(driver):
    driver.find_element_by_accessibility_id('activityCompletedButton').click()


def check_out(driver):
    time.sleep(1)
    driver.find_element_by_accessibility_id('Check-Out').click()
    time.sleep(5)
    setting_contact(driver)
    time.sleep(5)
    activity_complete(driver)

    user_action = TouchAction(driver)
    user_action.tap(x=450, y=906).perform()