import time
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

i=1
def start_server():
    # if server is already started in some port then it will not show error and requests will be sent to that paticular server

    os.system("start /B start cmd.exe @cmd /k appium")
    #time.sleep(5)

def settingup():

    desired_capabilities = {

        "app": "C:\\Users\\veris\\Downloads\\Latest_Release_Updated\\Terminal-Plus-release (4).apk",
        "platformName": "Android",
        "deviceName": "92ddcb31",
        "appActivity": ".MainActivity",
        "appPackage": "com.veristerminal",
        "unicodeKeyboard": False,
        " resetKeyboard": False,
        "platformVersion": "7.1.1",
        "appiumVersion": "1.12.1"
    }
    walkin_details = {
        "firstname": "tone",
        "lastname": "ttwo",
        "email": "tt@st.com",
        "unique_id":"test111",
        "address":"JMD",
        "Emergency_contact_name":"TOM",
        "Emergency_contact":"9988776655",
        "status":"walkin"
    }
    member_details = {
        "firstname": "mansi",
        "lastname": "sahu",
        "email": "mansisahu1480@gmail.com",
        "phone":"9993483676",
        "unique_id":"m123",
        "Emergency_contact_name": "test name",
        "Emergency_contact": "9992223331",
        "status":"member"
    }
    invited_details = {
        "firstname": "test_invite",
        "lastname": "test_invite_surname",
        "email": "testinvite@a.nn",
        "phone":"3333333333",
        "status":"invite"
    }
    offline_walkin_details = {
        "firstname": "offone",
        "lastname": "offtwo",
        "email": "off@t.co",
        "unique_id": "test111",
        "address": "JMD",
        "Emergency_contact_name": "TOM",
        "Emergency_contact": "9988776655",
        "status": "offline"
    }

    data={}
    data['desired_capabilities']=desired_capabilities
    data['walkin_details']=walkin_details
    data['member_details']=member_details
    data['invited_details']=invited_details
    data['offline_walkin_details']=offline_walkin_details
    return data

def offline_mode(driver):
    status = "offline"
    settings = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "settingsButton")))
    settings.click()
    code = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "authorizationCode")))
    code.send_keys("1")
    settings = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "settings")))
    settings.click()
    settings = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "switchToOfflineMode")))
    settings.click()
    done = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Done")))
    done.click()
    time.sleep(0.5)
    driver.toggle_wifi()
def statusOftest(status_test,driver):
    if (status_test == False):
        print("test case failed")
        a = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Cancel')))
        a.click()
        time.sleep(1)
        assert True
    else:
        print("test case passed")

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
    time.sleep(1.5)
    driver.press_keycode(4)
    time.sleep(0.5)
    driver.start_activity("com.veristerminal", ".MainActivity")
    #time.sleep(10)
    element_id=WebDriverWait(driver, 20,poll_frequency=0.5).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID,"Authorization ID")))
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
    takeScreenshot(driver)
    checkin.click()
    assert True
def setting_contact_invite(driver):
    phone=WebDriverWait(driver, 3, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID,'enterMobileNumber')))
    phone.click()
    for i in range(10):
        no=WebDriverWait(driver, 10, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID,"3")))
        no.click()

    next=WebDriverWait(driver, 2, poll_frequency=0.05).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID,"checkmark")))
    takeScreenshot(driver)
    next.click()
def setting_contact(driver):
    phone = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'enterMobileNumber')))
    phone.click()
    contact_no = ""
    i="7"
    j="zeroButton"
    for k in range(4):
        driver.find_element_by_accessibility_id(i).click()
        contact_no=contact_no+i
    for k in range(6):

        driver.find_element_by_accessibility_id(j).click()
        if(j == 'zeroButton'):
            contact_no=contact_no+"0"
        else:
            contact_no = contact_no + j
    #next = WebDriverWait(driver, 2, poll_frequency=0.05).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "checkmark")))
    #next.click()
    takeScreenshot(driver)
    driver.find_element_by_accessibility_id('checkmark').click()
    assert True
    return contact_no

def setting_contact_offline(driver):
    phone = WebDriverWait(driver, 10, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'enterMobileNumber')))
    phone.click()
    contact_no = ""
    i="9"
    j="1"
    for k in range(5):
        driver.find_element_by_accessibility_id(i).click()
        contact_no=contact_no+i
    for k in range(5):

        driver.find_element_by_accessibility_id(j).click()
        contact_no = contact_no + j
    #next = WebDriverWait(driver, 2, poll_frequency=0.05).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "checkmark")))
    #next.click()
    takeScreenshot(driver)
    driver.find_element_by_accessibility_id('checkmark').click()
    assert True
    return contact_no

def setting_contact_member(driver):
    phone = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'enterMobileNumber')))
    phone.click()
    time.sleep(0.05)
    driver.find_element_by_accessibility_id("9").click()
    driver.find_element_by_accessibility_id("9").click()
    driver.find_element_by_accessibility_id("9").click()
    driver.find_element_by_accessibility_id("3").click()
    driver.find_element_by_accessibility_id("4").click()
    driver.find_element_by_accessibility_id("8").click()
    driver.find_element_by_accessibility_id("3").click()
    driver.find_element_by_accessibility_id("6").click()
    driver.find_element_by_accessibility_id("7").click()
    driver.find_element_by_accessibility_id("6").click()
    takeScreenshot(driver)
    next = WebDriverWait(driver, 2, poll_frequency=0.05).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "checkmark")))
    next.click()
    assert True

def walkin_visitor(driver,walkin_details):
    try:
        status = walkin_details['status']
        user_action = TouchAction(driver)
        checkIn(driver)
        if (status == 'walkin'):
            contact = setting_contact(driver)

        elif (status == 'offline'):
            contact = setting_contact_offline(driver)

        visitor = WebDriverWait(driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Visitor")))
        takeScreenshot(driver)
        if (visitor.is_displayed()):
            assert True
            visitor.click()
        else:
            assert False
        camera(driver)

        FLEP_Screen(driver, walkin_details, contact)
        if (status == 'walkin'):
            Meeting_with_screen(driver)
        elif (status == 'offline'):
            Meeting_with_offline_screen(driver)
        unique_id(driver, walkin_details['unique_id'])
        gender_Screen(driver)
        Multi_select_screen(driver)
        GOVT_Id_Screen(driver)
        single_dropdown_screen(driver)
        driver.find_element_by_accessibility_id('Address').send_keys(walkin_details['address'])
        driver.hide_keyboard()
        emergency_contact(driver, walkin_details)
        rating_Screen(driver)
        time.sleep(0.05)
        takeScreenshot(driver)
        next = WebDriverWait(driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, "nextButton")))
        next.click()
        multi_tenant(driver)
        NDA_screen(driver)
        time.sleep(1)
        takeScreenshot(driver)
        user_action.tap(x=285, y=809).perform()
        time.sleep(0.5)
        user_action.tap(x=482, y=810).perform()
        date_and_time(driver)
        activity_complete(driver, walkin_details)
        check_out(driver, walkin_details)
        status_test = True
        statusOftest(status_test, driver)
    except:
        status_test = False
        takeScreenshotError(driver)
        statusOftest(status_test, driver)
        raise

def autofetch_user(driver,walkin_details):

    status=walkin_details['status']
    try:
        user_action = TouchAction(driver)
        checkIn(driver)
        if(status == 'walkin'):
            contact = setting_contact(driver)
        elif(status == 'offline'):
            contact = setting_contact_offline(driver)
        visitor = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Visitor")))
        takeScreenshot(driver)
        if (visitor.is_displayed()):
            assert True
            visitor.click()
        else:
            assert False
        cameraretake(driver)
        FLEP_auto_fetch_visitor(driver, walkin_details, contact)
        if(status == 'walkin'):
            Meeting_with_screen(driver)
        elif (status == 'offline'):
            Meeting_with_offline_screen(driver)
        unique_id_autofetch(driver, walkin_details['unique_id'])
        gender_Screen(driver)
        Multi_select_screen(driver)
        Govt_Id_Retake(driver)
        single_dropdown_screen(driver)
        address = driver.find_element_by_xpath(
            '//android.view.ViewGroup[@content-desc="Address"]/android.widget.EditText')
        my_address = address.text
        print(my_address)
        assert my_address == walkin_details['address']
        emergency_details_autofetch(driver, walkin_details)
        rating_Screen(driver)
        time.sleep(0.05)
        takeScreenshot(driver)
        next = WebDriverWait(driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, "nextButton")))
        next.click()
        multi_tenant(driver)
        NDA_screen(driver)
        user_action.tap(x=285, y=809).perform()
        time.sleep(0.5)
        takeScreenshot(driver)
        user_action.tap(x=482, y=810).perform()
        date_and_time(driver)
        activity_complete(driver, walkin_details)
        check_out(driver, walkin_details)
        status_test = True
        statusOftest(status_test, driver)
    except:
        print("exception")
        status_test = False
        statusOftest(status_test, driver)
        raise

def camera(driver):
    image=WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "clickImageButton")))
    if(image.is_displayed()):
        assert True
        image.click()
    else:
        assert False
    btn=WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "nextButton")))
    takeScreenshot(driver)
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
    takeScreenshot(driver)
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
    Phone = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Phone Number"]/android.widget.EditText')
    num = Phone.text
    print(num)
    assert num == contact
    #time.sleep(3)
    takeScreenshot(driver)
    driver.find_element_by_accessibility_id('nextButton').click()
    #time.sleep(2)

def FLEP_auto_fetch_member(driver,member_details):
    #time.sleep(5)
    Fname=WebDriverWait(driver, 3, poll_frequency=0.005).until(EC.presence_of_element_located((By.XPATH, "//android.view.ViewGroup[@content-desc='First Name']/android.widget.EditText")))
    #Fname = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="First Name"]/android.widget.EditText')
    text = Fname.text
    print(text)
    #print(member_details['firstname'])
    assert text == member_details['firstname']
    #time.sleep(3)
    Lname = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Last Name"]/android.widget.EditText')
    status = Lname.is_displayed()
    print(status)
    text1 = Lname.text
    print(text1)
    assert text1 == member_details['lastname']
    email = WebDriverWait(driver, 2, poll_frequency=0.05).until(EC.presence_of_element_located((By.XPATH, '//android.view.ViewGroup[@content-desc="Email"]/android.widget.EditText')))
    #Email = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Email"]/android.widget.EditText')
    text2 = email.text
    print(text2)
    if (len(text2) == 0):
        driver.set_value(email,'testinvite@a.nn')
        #time.sleep(0.5)
    else:
        if (len(text2) > 0 and text2 == member_details['email']):
            assert True
        else:
            assert False

    #time.sleep(3)
    Phone = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Phone Number"]/android.widget.EditText')
    text4 = Phone.text
    print(text4)
    if (len(text4) > 0 and text4 == member_details['phone']):
        assert True
        #print("Contact autofetched test case passed")
    else:
        assert False
        print("Contact autofetched test case failed")

    #time.sleep(2)
    takeScreenshot(driver)
    driver.find_element_by_accessibility_id('nextButton').click()
    #time.sleep(2)

def FLEP_auto_fetch_visitor(driver,visitor_details,contact_no):
    #time.sleep(5)
    #Fname = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="First Name"]/android.widget.EditText')
    Fname = WebDriverWait(driver, 3, poll_frequency=0.005).until(EC.presence_of_element_located((By.XPATH, "//android.view.ViewGroup[@content-desc='First Name']/android.widget.EditText")))

    text = Fname.text
    print(text)
    assert text == visitor_details['firstname']
    """if (len(text) > 0 and text == visitor_details['firstname']):
        print("Fname autofetched test case passed")
    else:
        print("Fname autofetched test case failed")"""

    Lname = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Last Name"]/android.widget.EditText')
    text1 = Lname.text
    print(text1)
    assert text1 == visitor_details['lastname']
    """if (len(text1) > 0 and text1 == visitor_details['lastname']):
        print("Lname autofetched test case passed")
    else:
        print("Lname autofetched test case failed")
    """
    Email = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Email"]/android.widget.EditText')
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
    text4 = Phone.text
    print(text4)
    assert text4 == contact_no
    """if (len(text4) > 0 and Phone == visitor_details['phone']):
        print("Contact autofetched test case passed")
    else:
        print("Contact autofetched test case failed")
    """
    #time.sleep(1)
    takeScreenshot(driver)
    driver.find_element_by_accessibility_id('nextButton').click()
    #time.sleep(2)

def Meeting_with_screen(driver):

    meeting = driver.find_element_by_accessibility_id('Whom To Meet')
    driver.set_value(meeting, "man")
    #time.sleep(3)
    el=WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.XPATH, '//android.view.ViewGroup[@content-desc="losmansi sahu"]/android.view.ViewGroup/android.widget.TextView[1]')))
    el.click()
    driver.hide_keyboard()

def Meeting_with_offline_screen(driver):

    meeting = driver.find_element_by_accessibility_id('Whom To Meet')
    driver.set_value(meeting, "man")
    #time.sleep(3)
    el=WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.XPATH, '//android.view.ViewGroup[@content-desc="meetingWithDropdownField"]/android.view.ViewGroup')))
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
    takeScreenshot(driver)
    b.click()
    assert True
    #driver.find_element_by_accessibility_id('nextButton').click()

def multi_tenant(driver):
    s=WebDriverWait(driver, 10, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.XPATH, '//android.view.ViewGroup[@content-desc="searchBar"]/android.widget.EditText')))
    s.send_keys('Man')
    a = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Mansi Test")))
    takeScreenshot(driver)
    a.click()
def takeScreenshot(driver):
    """ts=time.strftime("%Y_%m_%d_%H:%M:%S")
    activity=driver.current_activity
    screenshotBase64 = driver.get_screenshot_as_base64()
    """
    #file_name = ts + activity+screenshotBase64
    #print(file_name)
    #//pytestpackage/screenshot
    #ts = time.strftime("%Y_%m_%d_%H::%M::%S")
    global i
    #ts = time.strftime("%Y_%m_%d_%H:%M:%S")
    filename="./screenshots/test_"+str(i)+'.png'

    try:

        driver.save_screenshot(filename)
        print("saved =>"+filename)

    except NotADirectoryError:
        print("Not a directory")
    i = i + 1
    #print("screenshot saved")

def takeScreenshotError(driver):
    global j
    j=1
    filename = "./errors/errtest_" + str(j) + '.png'
    try:
        driver.save_screenshot(filename)
        print("saved =>" + filename)

    except NotADirectoryError:
        print("Not a directory")
    j = j + 1

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
    time.sleep(1)
    takeScreenshot(driver)
    user_action.tap(x=375, y=989).perform()
    #time.sleep(2)
def date_and_time(driver):
    #time.sleep(2)
    p=WebDriverWait(driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup')))
    p.click()
    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup').click()
    #time.sleep(2)
    p = WebDriverWait(driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]')))
    takeScreenshot(driver)
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
    takeScreenshot(driver)
    b.click()
   # driver.find_element_by_accessibility_id("cardScanNextButton").click()
    #time.sleep(5)

def Govt_Id_Retake(driver):
    #time.sleep(5)
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
    takeScreenshot(driver)
    b.click()
    # driver.find_element_by_accessibility_id("cardScanNextButton").click()
    #time.sleep(2)
def activity_complete(driver,details):
    #driver.find_element_by_accessibility_id('activityCompletedButton').click()
    a = WebDriverWait(driver, 3, poll_frequency=0.05).until(
        EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]")))
    texts=a.text
    print(texts)
    a=details['firstname']
    b=details['lastname']
    if(a in texts and b in texts):
        b = WebDriverWait(driver, 3, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID,"activityCompletedButton")))
        takeScreenshot(driver)
        b.click()
        assert True
    else:
        assert False


def check_out(driver,details):
    #time.sleep(1)
    #driver.find_element_by_accessibility_id('Check-Out').click()
    checkin = WebDriverWait(driver, 10, poll_frequency=0.05).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Check-Out")))
    takeScreenshot(driver)
    checkin.click()
    assert True
    if(details['status'] == 'walkin'):
        setting_contact(driver)
    elif(details['status'] == 'invite'):
        setting_contact_invite(driver)
    elif (details['status'] == 'member'):
        setting_contact_member(driver)

    elif (details['status'] == 'offline'):
        setting_contact_offline(driver)
    #time.sleep(5)
    activity_complete(driver,details)

    user_action = TouchAction(driver)
    takeScreenshot(driver)
    user_action.tap(x=450, y=906).perform()

def emergency_details_autofetch(driver,walkin_details):

    #print('Inside emergency code ')
    #time.sleep(3)
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
    #time.sleep(2)
    emer_phone = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Emergency contact"]/android.widget.EditText')
    phone = emer_phone.text
    print(phone)
    assert phone == walkin_details['Emergency_contact']
    """if (len(phone) > 0):
        print("Emergency phone test case passed")
    else:
        print("Emergency phone case failed")
    """
def general_activity_dropdown(driver):
    try:
        useraction = TouchAction(driver)
        e = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH, '(//android.view.ViewGroup[@content-desc="dropdownFormComponentField"])[1]/android.view.ViewGroup')))
        e.click()
        el = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]")))
        el.click()
        e2 = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,'(//android.view.ViewGroup[@content-desc="dropdownFormComponentField"])[2]/android.view.ViewGroup')))
        e2.click()
        e3 = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,                                                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup[1]')))
        e3.click()

        """
        time.sleep(4)
        #useraction.tap(172, 196).perform()
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()
        #	(//android.view.ViewGroup[@content-desc="dropdownFormComponentField"])[2]/android.view.ViewGroup
        time.sleep(3)
        g=driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="dropdownFormComponentField"])[2]/android.view.ViewGroup')
        #g = WebDriverWait(driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH, '(//android.view.ViewGroup[@content-desc="dropdownFormComponentField"])[2]/android.view.ViewGroup')))
        g.click()
        time.sleep(4)
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup[1]').click()
        #useraction.tap(270, 196).perform()
        """
    except:
        print("Unable to select dropdown field")
        time.sleep(0.5)
        #e=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button').click()
        #e.click()
        raise

def logout(driver):
    settings = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "settingsButton")))
    settings.click()
    settings = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Authorization Code")))
    settings.send_keys("1")
    driver.hide_keyboard()
    settings = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "settings")))
    settings.click()
    settings = WebDriverWait(driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                  '//android.view.ViewGroup[@content-desc="logOutTerminal"]/android.view.ViewGroup/android.view.ViewGroup')))
    settings.click()
    c = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ID, "android:id/button1")))
    c.click()

    """
    driver.find_element_by_accessibility_id('settingsButton').click()
    #time.sleep(3)
    driver.find_element_by_accessibility_id('Authorization Code').send_keys("1")
    time.sleep(1)
    driver.hide_keyboard()
    time.sleep(2)
    driver.find_element_by_accessibility_id('settings').click()
    time.sleep(2)
    driver.find_element_by_xpath(
        '//android.view.ViewGroup[@content-desc="logOutTerminal"]/android.view.ViewGroup/android.view.ViewGroup').click()
    time.sleep(2)
    driver.find_element_by_id('android:id/button1').click()
    time.sleep(2)
    """
