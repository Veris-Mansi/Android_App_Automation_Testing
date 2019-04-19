import time
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

global driver

def start_server():
    # if server is already started in some port then it will not show error and requests will be sent to that paticular server

    os.system("start /B start cmd.exe @cmd /k appium")
    time.sleep(5)
def logout(driver):

    time.sleep(10)
    driver.find_element_by_accessibility_id('settingsButton').click()
    time.sleep(3)
    driver.find_element_by_accessibility_id('Authorization Code').send_keys("1")
    time.sleep(1)
    driver.hide_keyboard()
    time.sleep(2)
    driver.find_element_by_accessibility_id('settings').click()
    time.sleep(2)
    driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="logOutTerminal"]/android.view.ViewGroup/android.view.ViewGroup').click()
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
    data={}
    data['desired_capabilities']=desired_capabilities
    data['walkin_details']=walkin_details
    data['member_details']=member_details
    return data
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
    driver.find_element_by_accessibility_id("8").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("1").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("3").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("8").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("6").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("9").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("7").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("1").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("4").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("9").click()
    time.sleep(1)

    driver.find_element_by_accessibility_id("checkmark").click()

def date_and_time(driver):
    time.sleep(2)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup').click()
    time.sleep(2)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]').click()
    #today_date=date.text
    #print(today_date)

    time.sleep(3)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup').click()
    time.sleep(2)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TimePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]').click()
    #today_time=times.text
    #print(today_time)
    time.sleep(1)
    driver.find_element_by_accessibility_id('nextButton').click()
    time.sleep(4)
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

def Meeting_with_screen(driver):

    meeting = driver.find_element_by_accessibility_id('Whom To Meet')
    driver.set_value(meeting, "zxc")
    time.sleep(3)
    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]').click()
    driver.find_element_by_accessibility_id('meetingWithDropdownField').click()
    time.sleep(3)
    driver.hide_keyboard()
    time.sleep(1)

def Multi_select_screen(driver):
    driver.find_element_by_accessibility_id('dropdownFormComponentField').click()
    time.sleep(5)
    user_action = TouchAction(driver)
    user_action.tap(x=401, y=158).release().perform()
    time.sleep(3)
    user_action.tap(x=401, y=201).release().perform()
    time.sleep(3)

    user_action.tap(x=401, y=1205).release().perform()
    time.sleep(3)
    driver.find_element_by_accessibility_id('nextButton').click()
    time.sleep(3)

def single_dropdown_screen(driver):

    driver.find_element_by_accessibility_id('dropdownFormComponentField').click()
    time.sleep(5)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
    # user_action.tap(x=400,y=203).release().perform()
    time.sleep(2)
    user_action = TouchAction(driver)
    user_action.tap(x=403, y=1211).release().perform()
    # driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button').click()
    # user_action.perform(x=400,y=1211).release().perform()
    time.sleep(2)

def General_Activity_Member(driver,member_details):

    time.sleep(3)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView').click()
    setting_contact_member(driver)
    time.sleep(2)
    FLEP_auto_fetch_member(driver,member_details)
    time.sleep(3)
    emergency_details_autofetch(driver)
    time.sleep(2)
    unique_id_autofetch(driver)
    time.sleep(3)
    gender_Screen(driver)
    time.sleep(3)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[5]').click()
    time.sleep(2)
    driver.find_element_by_xpath('	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
    time.sleep(1)
    user_action=TouchAction(driver)
    user_action.tap(x=399,y=1215).perform()
    time.sleep(2)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[6]').click()
    time.sleep(2)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
    time.sleep(2)
    user_action.tap(x=399, y=1215).perform()
    time.sleep(2)
    driver.find_element_by_accessibility_id('nextButton').click()
    time.sleep(3)
    camera(driver)
    time.sleep(2)
    activity_complete(driver)
    time.sleep(2)
def rating_Screen(driver):
    time.sleep(2)
    listss = driver.find_elements_by_xpath(
        '//android.view.ViewGroup[@content-desc="ratingField"]/android.widget.Button')
    print(len(listss))
    listss[3].click()
    time.sleep(1)

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
def walk_in_visitor(driver,walkin_details):

    user_action=TouchAction(driver)
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
    checkIn(driver)
    time.sleep(3)
    setting_contact(driver)
    time.sleep(7)
    driver.find_element_by_accessibility_id("Visitor").click()
    time.sleep(3)

    camera(driver)
    time.sleep(2)
    FLEP_Screen(driver,walkin_details)
    time.sleep(3)
    Meeting_with_screen(driver)
    time.sleep(2)
    id =driver.find_element_by_accessibility_id('Unique_id')
    driver.set_value(id,'test111')
    time.sleep(2)

    driver.execute_script('mobile:performEditorAction', {'action': 'done'})
    time.sleep(1)
    gender_Screen(driver)
    time.sleep(3)
    Multi_select_screen(driver)
    time.sleep(1)
    cardScanning(driver)
    time.sleep(1)
    single_dropdown_screen(driver)
    time.sleep(2)
    driver.find_element_by_accessibility_id('Address').send_keys('JMD')
    driver.execute_script('mobile:performEditorAction', {'action': 'done'})
    time.sleep(2)
    driver.find_element_by_accessibility_id('Emergency contact name').send_keys('TOM')
    driver.execute_script('mobile:performEditorAction', {'action': 'done'})
    time.sleep(1)
    driver.find_element_by_accessibility_id('Emergency contact').send_keys('9988776655')
    driver.execute_script('mobile:performEditorAction', {'action': 'done'})
    time.sleep(1)
    rating_Screen(driver)
    time.sleep(1)
    driver.find_element_by_accessibility_id('nextButton').click()
    time.sleep(3)
    driver.find_element_by_accessibility_id('Mansi Test').click()
    time.sleep(8)
    NDA_screen(driver)
    time.sleep(5)
    user_action.tap(x=296, y=1029).perform()
    time.sleep(3)
    user_action.tap(x=492,y=1033).perform()
    #driver.find_element_by_accessibility_id('printButton').click()
    #time.sleep(5)
    #driver.find_element_by_accessibility_id('nextButton').click()
    time.sleep(5)
    date_and_time(driver)
    activity_complete(driver)
    time.sleep(3)

    #user_action.tap(x=450, y=906).perform()
    #time.sleep(10)

    check_out(driver)
    time.sleep(10)

def check_out(driver):
    time.sleep(1)
    driver.find_element_by_accessibility_id('Check-Out').click()
    time.sleep(5)
    setting_contact(driver)
    time.sleep(5)
    activity_complete(driver)

    user_action = TouchAction(driver)
    user_action.tap(x=450, y=906).perform()

def invited_user(driver):
    checkIn(driver)
    time.sleep(3)
    driver.find_element_by_accessibility_id('').click()
    time.sleep(3)
    driver.find_element_by_accessibility_id('Invited').click()
    #FLEP SCREEN
    #Meeting with

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
    if (len(text4) > 0):
        print("Contact autofetched test case passed")
    else:
        print("Contact autofetched test case failed")

    time.sleep(2)
    driver.find_element_by_accessibility_id('nextButton').click()
    time.sleep(2)

def emergency_details_autofetch(driver):
    print('Inside emergency code ')
    time.sleep(3)
    #emer_name = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Emergency contact name"]/android.widget.EditText')
    emer_name=driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Emergency Contact Name"]/android.widget.EditText')
    status=emer_name.is_displayed()
    print(status)
    name = emer_name.text
    print(name)
    if (len(name) > 0):
        print("Emergency name test case passed")
    else:
        print("Emergency name case failed")

    time.sleep(2)
    emer_phone = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Emergency contact"]/android.widget.EditText')
    phone = emer_phone.text
    print(phone)
    if (len(phone) > 0):
        print("Emergency phone test case passed")
    else:
        print("Emergency phone case failed")

def unique_id_autofetch(driver):
    time.sleep(1)
    id = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Unique_id"]/android.widget.EditText')
    my_id = id.text
    print(my_id)
    if (len(my_id) > 0):
        print("Unique_id test case passed")
    else:
        print("Unique_id test case failed")

    time.sleep(1)
def auto_fetch_user(driver,walkin_details):

    status="Visitor"
    """time.sleep(5)
    permission_buttons(driver)
    # time.sleep(2)
    # driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
    user_action=TouchAction(driver)
    time.sleep(10)
    driver.press_keycode(4)
    time.sleep(2)

    driver.start_activity("com.veristerminal", ".MainActivity")
    time.sleep(10)
    # (new TouchAction(driver)).tap(385, 676).perform()
    login(driver)
    time.sleep(10)"""
    time.sleep(3)
    checkIn(driver)
    time.sleep(5)
    setting_contact(driver)
    time.sleep(3)
    driver.find_element_by_accessibility_id('Visitor').click()
    retakeButton = driver.find_element_by_accessibility_id("retakeButton")
    status = retakeButton.is_displayed()
    print(status)
    if (status):
        print("Image autofetched test case passed")
    else:
        print("Image not autofetched test case failed")

    time.sleep(5)
    driver.find_element_by_accessibility_id("nextButton").click()
    time.sleep(4)
    FLEP_auto_fetch_visitor(driver,walkin_details)
    time.sleep(3)
    Meeting_with_screen(driver)
    time.sleep(1)
    unique_id_autofetch(driver)

    time.sleep(2)
    gender_Screen(driver)
    time.sleep(2)
    Multi_select_screen(driver)
    time.sleep(3)
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
    single_dropdown_screen(driver)
    time.sleep(3)
    address = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Address"]/android.widget.EditText')
    my_address=address.text

    print(my_address)
    if(len(my_address) > 0):
        print("Address test case passed")
    else:
        print("Address test case failed")
    time.sleep(3)
    emergency_details_autofetch(driver)
    time.sleep(3)
    rating_Screen(driver)
    driver.find_element_by_accessibility_id('nextButton').click()
    time.sleep(2)
    driver.find_element_by_accessibility_id('Mansi Test').click()
    time.sleep(8)
    NDA_screen(driver)
    time.sleep(5)
    user_action=TouchAction(driver)
    user_action.tap(x=296, y=1029).perform()
    time.sleep(3)
    user_action.tap(x=492, y=1033).perform()
    # driver.find_element_by_accessibility_id('printButton').click()
    # time.sleep(5)
    # driver.find_element_by_accessibility_id('nextButton').click()
    time.sleep(2)
    activity_complete(driver)
    time.sleep(3)
    check_out(driver)
    time.sleep(10)

def kill_server(driver):
    driver.execute_script('mobile: shell', {
        'command': 'echo',
        'args': ['arg1', 'arg2'],
        'includeStderr': True,
        'timeout': 5000
    })
    print("server_killed")
def main():

    start_server()
    time.sleep(2)
    data={}
    data = settingup()
    driver=launch_application(data['desired_capabilities'])
    walk_in_visitor(driver,data['walkin_details'])
    time.sleep(10)
    auto_fetch_user(driver,data['walkin_details'])
    time.sleep(7)
    General_Activity_Member(driver,data['member_details'])
    #logout(driver)
    #kill_server(driver)
    #auto_fetch_walkin(driver)

if __name__ == "__main__":
    main()
