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
    #time.sleep(5)

def settingup():

    desired_capabilities = {

        "app": "C:\\Users\\veris\\Downloads\\updated_release2\\Terminal-Plus-release (4).apk",
        "platformName": "Android",
        "deviceName": "RZ8M30B0LNZ",
        "appActivity": ".MainActivity",
        "appPackage": "com.veristerminal",
        "unicodeKeyboard": False,
        " resetKeyboard": False,
        "platformVersion": "9",
        "appiumVersion": "1.12.1"
    }
    walkin_details = {
        "firstname": "test_one",
        "lastname": "test_surname",
        "email": "test@test.com",
        "unique_id":"test111",
        "address":"JMD",
        "Emergency_contact_name":"TOM",
        "Emergency_contact":"9988776655"
    }
    member_details = {
        "firstname": "mansi",
        "lastname": "sahu",
        "email": "mansisahu1480@gmail.com",
        "phone":"9993483676",
        "unique_id":"m123",
        "Emergency_contact_name": "test name",
        "Emergency_contact": "9992223331"
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
        time.sleep(0.05)

def launch_application(desired_capabilities):
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
    return driver

def login(driver):
    time.sleep(0.5)
    permission_buttons(driver)
    time.sleep(1)
    driver.press_keycode(4)
    time.sleep(0.5)
    driver.start_activity("com.veristerminal", ".MainActivity")
    #time.sleep(10)
    element_id=WebDriverWait(driver, 10,poll_frequency=0.5).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID,"Authorization ID")))
    #element_id = driver.find_element_by_accessibility_id("Authorization ID")
    element_id.send_keys('N1')
    driver.hide_keyboard()
    driver.find_element_by_accessibility_id('Authorization Code').send_keys('1')
    #element_code=WebDriverWait(driver,2,poll_frequency=0.05).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID,"Authorization Code")))
    #element_code.send_keys('1')
    driver.hide_keyboard()
    driver.find_element_by_accessibility_id("loginButton").click()
    assert True
def checkIn(driver):

    checkin=WebDriverWait(driver, 10, poll_frequency=0.05).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID,"Check-In")))
    checkin.click()
    assert True
def setting_contact_invite(driver):
    phone=WebDriverWait(driver, 3, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID,'enterMobileNumber')))
    phone.click()
    for i in range(10):
        no=WebDriverWait(driver, 10, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID,"3")))
        no.click()

    next=WebDriverWait(driver, 2, poll_frequency=0.05).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID,"checkmark")))
    next.click()
def setting_contact(driver):
    phone = WebDriverWait(driver, 1, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'enterMobileNumber')))
    phone.click()
    contact_no = ""
    i="7"
    j="2"
    for k in range(5):
        driver.find_element_by_accessibility_id(i).click()
        contact_no=contact_no+i
    for k in range(5):

        driver.find_element_by_accessibility_id(j).click()
        contact_no = contact_no + j
    #next = WebDriverWait(driver, 2, poll_frequency=0.05).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "checkmark")))
    #next.click()
    driver.find_element_by_accessibility_id('checkmark').click()
    assert True
    return contact_no
def setting_contact_member(driver):
    phone = WebDriverWait(driver, 3, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'enterMobileNumber')))
    phone.click()

    no = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 9)))
    no.click()
    no = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 9)))
    no.click()

    no = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 9)))
    no.click()

    no = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 3)))
    no.click()

    no = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 4)))
    no.click()

    no = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 8)))
    no.click()

    no = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 3)))
    no.click()

    no = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 6)))
    no.click()

    no = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 7)))
    no.click()

    no = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 6)))
    no.click()

    driver.find_element_by_accessibility_id("checkmark").click()
    next = WebDriverWait(driver, 2, poll_frequency=0.05).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "checkmark")))
    next.click()
    assert True
def camera(driver):
    image=WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "clickImageButton")))
    if(image.is_displayed()):
        assert True
        image.click()
    else:
        assert False
    btn=WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "nextButton")))
    btn.click()
    assert True
    #time.sleep(10)
def cameraretake(driver):
    retakeButton = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "retakeButton")))
    status = retakeButton.is_displayed()
    if (status):
        assert True
    else:
        print("Image not autofetched test case failed")
        assert False
    btn = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "nextButton")))
    btn.click()
    assert True


def FLEP_Screen(driver,walkin_details,contact):
    """FirstName = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "First Name")))
    FirstName.send_keys(walkin_details['firstname'])
    LastName = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Last Name")))
    LastName.send_keys(walkin_details['lastname'])
    email = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Email")))
    email.send_keys(walkin_details['email'])
    driver.hide_keyboard()
    contact_element = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Phone Number")))
    num=contact_element.get_attribute('text')
    assert num == contact
    btn = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "nextButton")))
    btn.click()
    assert True"""
    driver.find_element_by_accessibility_id('First Name').send_keys(walkin_details['firstname'])
    #time.sleep(2)
    driver.find_element_by_accessibility_id('Last Name').send_keys(walkin_details['lastname'])
    #time.sleep(2)
    driver.find_element_by_accessibility_id('Email').send_keys(walkin_details['email'])
    #time.sleep(2)
    driver.hide_keyboard()
    #time.sleep(2)
    Phone = driver.find_element_by_xpath(
        '//android.view.ViewGroup[@content-desc="Phone Number"]/android.widget.EditText')
    num = Phone.get_attribute('text')
    print(num)
    assert num == contact
    #time.sleep(3)
    driver.find_element_by_accessibility_id('nextButton').click()
    #time.sleep(2)

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

def FLEP_auto_fetch_visitor(driver,visitor_details,contact_no):
    time.sleep(5)
    Fname = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="First Name"]/android.widget.EditText')
    status = Fname.is_displayed()
    print(status)
    text = Fname.text
    print(text)
    assert text == visitor_details['firstname']
    """if (len(text) > 0 and text == visitor_details['firstname']):
        print("Fname autofetched test case passed")
    else:
        print("Fname autofetched test case failed")"""

    time.sleep(1)
    Lname = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Last Name"]/android.widget.EditText')
    status = Lname.is_displayed()
    print(status)
    text1 = Lname.text
    print(text1)
    assert text1 == visitor_details['lastname']
    """if (len(text1) > 0 and text1 == visitor_details['lastname']):
        print("Lname autofetched test case passed")
    else:
        print("Lname autofetched test case failed")
    """
    time.sleep(1)
    Email = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Email"]/android.widget.EditText')
    status = Email.is_displayed()
    print(status)
    text2 = Email.text
    print(text2)
    print(len(text2))
    if(text2 == 'Email'):
        driver.set_value(Email,'testinvite@a.nn')
        assert True
    else:
        assert text2 == visitor_details['email']
        """if (len(text2) > 0 and text2 == visitor_details['email']):
            print("Email autofetched test case passed")
        else:
            print("Email autofetched test case failed")"""

    time.sleep(1)
    Phone = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Phone Number"]/android.widget.EditText')
    status = Phone.is_displayed()
    print(status)
    text4 = Phone.text
    print(text4)
    assert text4 == contact_no
    """if (len(text4) > 0 and Phone == visitor_details['phone']):
        print("Contact autofetched test case passed")
    else:
        print("Contact autofetched test case failed")
    """
    time.sleep(1)
    driver.find_element_by_accessibility_id('nextButton').click()
    time.sleep(2)

def Meeting_with_screen(driver):

    meeting = driver.find_element_by_accessibility_id('Whom To Meet')
    driver.set_value(meeting, "man")
    #time.sleep(3)
    el=WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.XPATH, '//android.view.ViewGroup[@content-desc="losmansi sahu"]/android.view.ViewGroup/android.widget.TextView[1]')))
    el.click()
    driver.hide_keyboard()

def unique_id(driver,uniqueid):
    driver.find_element_by_accessibility_id('Unique_id').send_keys(uniqueid)

def unique_id_autofetch(driver,unique_id):
    uniqid=driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Unique_id"]/android.widget.EditText')
    my_id = uniqid.text
    print(my_id)
    assert my_id == unique_id

def gender_Screen(driver):
    gender = []
    gender = driver.find_elements_by_xpath(
        '//android.view.ViewGroup[@content-desc="radioButtonField"]/android.view.ViewGroup/android.view.ViewGroup')
    print(len(gender))
    status_radio = gender[0].is_selected()
    print(status_radio)
    if (status_radio == False):
        gender[0].click()
        assert True

def Multi_select_screen(driver):

    driver.find_element_by_accessibility_id('dropdownFormComponentField').click()
    #time.sleep(0.5)
    a=WebDriverWait(driver, 3, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]")))
    a.click()
    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()
    assert True
    b = WebDriverWait(driver, 3, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]")))
    b.click()
    #time.sleep(0.5)
    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
    assert True
    b = WebDriverWait(driver, 3, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button")))
    b.click()
    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button').click()
    assert True
    b = WebDriverWait(driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID,"nextButton")))
    b.click()
    assert True
    #driver.find_element_by_accessibility_id('nextButton').click()

def single_dropdown_screen(driver):

    driver.find_element_by_accessibility_id('dropdownFormComponentField').click()
    assert True
    #time.sleep(0.5)
    b = WebDriverWait(driver, 3, poll_frequency=0.005).until(EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]")))
    b.click()

    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
    # user_action.tap(x=400,y=203).release().perform()
    assert True
    #time.sleep(2)

def cardScanning(driver):
    driver.find_element_by_accessibility_id('cardScanClickImageButton').click()
    time.sleep(7)
    driver.find_element_by_accessibility_id('cardScanNextButton').click()
    time.sleep(3)
def rating_Screen(driver):
    time.sleep(0.5)
    listss = driver.find_elements_by_xpath(
        '//android.view.ViewGroup[@content-desc="ratingField"]/android.widget.Button')
    print(len(listss))
    listss[3].click()
    #time.sleep(1)

def emergency_contact(driver,walkin_details):

    driver.find_element_by_accessibility_id('Emergency contact name').send_keys(walkin_details['Emergency_contact_name'])
    #driver.execute_script('mobile:performEditorAction', {'action': 'done'})
    driver.hide_keyboard()
    #time.sleep(1)
    driver.find_element_by_accessibility_id('Emergency contact').send_keys(walkin_details['Emergency_contact'])
    driver.hide_keyboard()
    #driver.execute_script('mobile:performEditorAction', {'action': 'done'})
    #time.sleep(1)

def NDA_screen(driver):
    #driver.find_element_by_accessibility_id('signatureField')
    WebDriverWait(driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH, '//android.view.ViewGroup[@content-desc="signatureField"]/android.widget.LinearLayout/android.view.View')))
    #driver.find_elements_by_xpath('//android.view.ViewGroup[@content-desc="signatureField"]/android.widget.LinearLayout/android.view.View')
    #time.sleep(1)
    user_action=TouchAction(driver)
    user_action.press(x=240,y=791).move_to(x=369,y=739).release()
    time.sleep(5)
    user_action.tap(x=375, y=989).perform()
    #time.sleep(2)
def date_and_time(driver):
    #time.sleep(2)
    p=WebDriverWait(driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup')))
    p.click()
    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup').click()
    #time.sleep(2)
    p = WebDriverWait(driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]')))
    p.click()

    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]').click()

    #time.sleep(3)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup').click()
    #time.sleep(2)
    driver.find_element_by_id('android:id/button1').click()
    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TimePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]').click()
    #time.sleep(1)
    driver.find_element_by_accessibility_id('nextButton').click()
    #time.sleep(2)
def GOVT_Id_Screen(driver):
    b = WebDriverWait(driver, 10, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "cardScanClickImageButton")))
    b.click()
    #driver.find_element_by_accessibility_id("cardScanClickImageButton").click()
    #time.sleep(10)
    b = WebDriverWait(driver, 10, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "cardScanNextButton")))
    b.click()
   # driver.find_element_by_accessibility_id("cardScanNextButton").click()
    #time.sleep(5)

def Govt_Id_Retake(driver):
    time.sleep(5)
    retakeButton=WebDriverWait(driver, 10, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "cardScanRetakeButton")))
    #retakeButton = driver.find_element_by_accessibility_id("cardScanRetakeButton")
    status_card = retakeButton.is_displayed()
    print(status_card)
    if (status_card):
        assert True
        print("Image autofetched test case passed")
    else:
        assert False
        print("Image not autofetched test case failed")
    #time.sleep(10)
    b = WebDriverWait(driver, 10, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "cardScanNextButton")))
    b.click()
    # driver.find_element_by_accessibility_id("cardScanNextButton").click()
    #time.sleep(2)
def activity_complete(driver):
    #driver.find_element_by_accessibility_id('activityCompletedButton').click()
    b = WebDriverWait(driver, 3, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID,"activityCompletedButton")))
    b.click()

def check_out(driver):
    #time.sleep(1)
    #driver.find_element_by_accessibility_id('Check-Out').click()
    checkin = WebDriverWait(driver, 10, poll_frequency=0.05).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Check-Out")))
    checkin.click()
    assert True
    #time.sleep(5)
    setting_contact(driver)
    #time.sleep(5)
    activity_complete(driver)

    user_action = TouchAction(driver)
    user_action.tap(x=450, y=906).perform()

def emergency_details_autofetch(driver,walkin_details):

    print('Inside emergency code ')
    time.sleep(3)
    #emer_name = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Emergency contact name"]/android.widget.EditText')

    emer_name = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Emergency contact name"]/android.widget.EditText')

    name = emer_name.text
    print(name)
    """if (len(name) > 0):
        print("Emergency name test case passed")
    else:
        print("Emergency name case failed")
    """
    assert name == walkin_details['Emergency_contact_name']
    time.sleep(2)
    emer_phone = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Emergency contact"]/android.widget.EditText')
    phone = emer_phone.text
    print(phone)
    assert phone == walkin_details['Emergency_contact']
    """if (len(phone) > 0):
        print("Emergency phone test case passed")
    else:
        print("Emergency phone case failed")
    """