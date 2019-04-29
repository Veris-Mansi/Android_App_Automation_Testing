"""
If pytest will not find fixtures in class itself then it will check for the conf_test file
"""

import pytest
from utilities.Resources2 import *

@pytest.mark.usefixtures("data","driver")
class TestWalk_In():

    @pytest.fixture(autouse=True)
    def classSetup(self,data,driver):
        self.driver=driver
        self.data=data
        self.walkin_details=data['walkin_details']
        self.member_details=data['member_details']
        self.invited_details=data['invited_details']

    def test_login(self):
        time.sleep(2)
        login(self.driver)
        assert True

    """def test_walkin(self):
        self.status_test = False
        user_action = TouchAction(self.driver)
        checkIn(self.driver)
        contact=setting_contact(self.driver)
        visitor=WebDriverWait(self.driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Visitor")))
        takeScreenshot(self.driver)
        if(visitor.is_displayed()):
            assert True
            visitor.click()
        else:
            assert False
        camera(self.driver)
        FLEP_Screen(self.driver,self.walkin_details,contact)
        Meeting_with_screen(self.driver)
        unique_id(self.driver,self.walkin_details['unique_id'])
        gender_Screen(self.driver)
        Multi_select_screen(self.driver)
        GOVT_Id_Screen(self.driver)
        single_dropdown_screen(self.driver)
        self.driver.find_element_by_accessibility_id('Address').send_keys(self.walkin_details['address'])
        self.driver.hide_keyboard()
        emergency_contact(self.driver,self.walkin_details)
        rating_Screen(self.driver)
        time.sleep(0.05)
        takeScreenshot(self.driver)
        self.driver.find_element_by_accessibility_id('nextButton').click()
        a=WebDriverWait(self.driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Mansi Test")))
        takeScreenshot(self.driver)
        a.click()
        NDA_screen(self.driver)
        time.sleep(1)
        takeScreenshot(self.driver)
        user_action.tap(x=285, y=809).perform()
        time.sleep(0.5)
        takeScreenshot(self.driver)
        user_action.tap(x=482, y=810).perform()
        date_and_time(self.driver)
        activity_complete(self.driver)
        check_out(self.driver)
        self.status_test = True
        statusOftest(self.status_test,self.driver)"""
   
    """def test_autofetch_user(self):
        user_action = TouchAction(self.driver)
        checkIn(self.driver)
        contact = setting_contact(self.driver)
        visitor = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Visitor")))
        takeScreenshot(self.driver)
        if (visitor.is_displayed()):
            assert True
            visitor.click()
        else:
            assert False
        cameraretake(self.driver)
        FLEP_auto_fetch_visitor(self.driver,self.walkin_details,contact)
        Meeting_with_screen(self.driver)
        unique_id_autofetch(self.driver,self.walkin_details['unique_id'])
        gender_Screen(self.driver)
        Multi_select_screen(self.driver)
        Govt_Id_Retake(self.driver)
        single_dropdown_screen(self.driver)
        address = self.driver.find_element_by_xpath(
            '//android.view.ViewGroup[@content-desc="Address"]/android.widget.EditText')
        my_address = address.text

        print(my_address)
        assert my_address == self.walkin_details['address']
        emergency_details_autofetch(self.driver,self.walkin_details)
        rating_Screen(self.driver)
        time.sleep(0.05)
        takeScreenshot(self.driver)
        self.driver.find_element_by_accessibility_id('nextButton').click()
        a = WebDriverWait(self.driver, 5, poll_frequency=0.1).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Mansi Test")))
        takeScreenshot(self.driver)
        a.click()
        NDA_screen(self.driver)
        time.sleep(1)
        takeScreenshot(self.driver)
        user_action.tap(x=285, y=809).perform()
        time.sleep(0.5)
        takeScreenshot(self.driver)
        user_action.tap(x=482, y=810).perform()
        date_and_time(self.driver)
        activity_complete(self.driver)
        check_out(self.driver)
        self.status_test = True
        statusOftest(self.status_test, self.driver)"""

    """def test_member_check_in(self):

        user_action = TouchAction(self.driver)
        checkIn(self.driver)
        time.sleep(0.5)
        setting_contact_member(self.driver)
        cameraretake(self.driver)
        FLEP_auto_fetch_member(self.driver,self.member_details)
        emergency_details_autofetch(self.driver,self.member_details)
        unique_id_autofetch(self.driver, self.member_details['unique_id'])
        self.driver.find_element_by_accessibility_id('nextButton').click()
        NDA_screen(self.driver)
        Govt_Id_Retake(self.driver)
        time.sleep(1)
        takeScreenshot(self.driver)
        user_action.tap(x=285, y=809).perform()
        time.sleep(0.5)
        takeScreenshot(self.driver)
        user_action.tap(x=482, y=810).perform()
        activity_complete(self.driver)
        check_out(self.driver)
        self.status_test = True
        statusOftest(self.status_test, self.driver)
    """
    def test_invited_user(self):
        checkIn(self.driver)
        setting_contact_invite(self.driver)
        visitor = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Invited")))
        takeScreenshot(self.driver)
        if (visitor.is_displayed()):
            assert True
            visitor.click()
        else:
            assert False
        FLEP_auto_fetch_member(self.driver, self.invited_details)
        #time.sleep(2)
        meeting = self.driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Whom To Meet"]/android.widget.EditText')
        text = meeting.text
        if (len(text) > 0 and text == 'Mansi Sahu'):
            print("Meeting with test case passed")
            assert True
        else:
            print("Meeting with test case failed")
            assert False
        takeScreenshot(self.driver)
        self.driver.find_element_by_accessibility_id('nextButton').click()
        time.sleep(2)
        activity_complete(self.driver)

    def test_invited_autofetch(self):
        checkIn(self.driver)
        setting_contact_invite(self.driver)
        visitor = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Invited")))
        takeScreenshot(self.driver)
        if (visitor.is_displayed()):
            assert True
            visitor.click()
        else:
            assert False
        FLEP_auto_fetch_member(self.driver, self.invited_details)
        time.sleep(2)
        meeting = self.driver.find_element_by_xpath(
            '//android.view.ViewGroup[@content-desc="Whom To Meet"]/android.widget.EditText')
        text = meeting.text
        if (len(text) > 0 and text == 'Mansi Sahu'):
            print("Meeting with test case passed")
            assert True
        else:
            print("Meeting with test case failed")
            assert False
        takeScreenshot(self.driver)
        self.driver.find_element_by_accessibility_id('nextButton').click()
        time.sleep(2)
        activity_complete(self.driver)

    def test_general_activity_member(self):
        el=WebDriverWait(self.driver, 3, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView")))
        el.click()
        #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView').click()
        setting_contact_member(self.driver)
        #time.sleep(2)
        FLEP_auto_fetch_member(self.driver, self.member_details)
        #time.sleep(3)
        emergency_details_autofetch(self.driver, self.member_details)
        unique_id_autofetch(self.driver, self.member_details['unique_id'])
        #time.sleep(3)
        gender_Screen(self.driver)
        #time.sleep(3)
        general_activity_dropdown(self.driver)
        #self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
        #time.sleep(1)
        self.driver.find_element_by_accessibility_id('nextButton').click()
        #time.sleep(3)
        cameraretake(self.driver)
        #time.sleep(2)
        activity_complete(self.driver)
        #time.sleep(2)

    def test_general_activity_walkin(self):
        el = WebDriverWait(self.driver, 3, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView")))
        el.click()
        contact=setting_contact(self.driver)
        FLEP_Screen(self.driver,self.walkin_details,contact)
        emergency_contact(self.driver,self.walkin_details)
        unique_id(self.driver,self.walkin_details['unique_id'])
        gender_Screen(self.driver)
        general_activity_dropdown(self.driver)
        # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
        # time.sleep(1)
        self.driver.find_element_by_accessibility_id('nextButton').click()
        camera(self.driver)
        activity_complete(self.driver)

    def test_general_activity_autofetch(self):
        el = WebDriverWait(self.driver, 3, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView")))
        el.click()
        contact=setting_contact(self.driver)
        FLEP_auto_fetch_visitor(self.driver,self.walkin_details,contact)
        emergency_details_autofetch(self.driver,self.walkin_details)
        unique_id_autofetch(self.driver,self.walkin_details['unique_id'])
        gender_Screen(self.driver)
        general_activity_dropdown(self.driver)
        # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
        # time.sleep(1)
        self.driver.find_element_by_accessibility_id('nextButton').click()
        cameraretake(self.driver)
        activity_complete(self.driver)

    def test_offlineMode(self):



