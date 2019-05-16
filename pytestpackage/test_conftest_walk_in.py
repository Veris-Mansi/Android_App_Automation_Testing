"""
If pytest will not find fixtures in class itself then it will check for the conf_test file
"""

import pytest
import time
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
        self.offline_walkin_details=data['offline_walkin_details']

    def test_login(self):
        time.sleep(2)
        login(self.driver)
        assert True


    def test_walkin(self):
        try:
            self.status_test = False
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
            camera(self.driver)
            FLEP_Screen(self.driver, self.walkin_details, contact)
            Meeting_with_screen(self.driver)
            unique_id(self.driver, self.walkin_details['unique_id'])
            gender_Screen(self.driver)
            Multi_select_screen(self.driver)
            GOVT_Id_Screen(self.driver)
            single_dropdown_screen(self.driver)
            self.driver.find_element_by_accessibility_id('Address').send_keys(self.walkin_details['address'])
            self.driver.hide_keyboard()
            emergency_contact(self.driver, self.walkin_details)
            rating_Screen(self.driver)
            time.sleep(0.05)
            takeScreenshot(self.driver)
            self.driver.find_element_by_accessibility_id('nextButton').click()
            a = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Mansi Test")))
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
            activity_complete(self.driver, self.walkin_details)
            check_out(self.driver, self.walkin_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
        except:
            self.status_test = False
            takeScreenshotError(self.driver)
            statusOftest(self.status_test, self.driver)
            raise
   
    def test_autofetch_user(self):
        try:
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
            FLEP_auto_fetch_visitor(self.driver, self.walkin_details, contact)
            Meeting_with_screen(self.driver)
            unique_id_autofetch(self.driver, self.walkin_details['unique_id'])
            gender_Screen(self.driver)
            Multi_select_screen(self.driver)
            Govt_Id_Retake(self.driver)
            single_dropdown_screen(self.driver)
            address = self.driver.find_element_by_xpath(
                '//android.view.ViewGroup[@content-desc="Address"]/android.widget.EditText')
            my_address = address.text

            print(my_address)
            assert my_address == self.walkin_details['address']
            emergency_details_autofetch(self.driver, self.walkin_details)
            rating_Screen(self.driver)
            time.sleep(0.05)
            takeScreenshot(self.driver)
            self.driver.find_element_by_accessibility_id('nextButton').click()
            a = WebDriverWait(self.driver, 5, poll_frequency=0.1).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Mansi Test")))
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
            activity_complete(self.driver, self.walkin_details)
            check_out(self.driver, self.walkin_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
        except:
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise

    def test_member_check_in(self):

        try:
            user_action = TouchAction(self.driver)
            checkIn(self.driver)
            time.sleep(0.5)
            setting_contact_member(self.driver)
            cameraretake(self.driver)
            FLEP_auto_fetch_member(self.driver, self.member_details)
            emergency_details_autofetch(self.driver, self.member_details)
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
            activity_complete(self.driver, self.member_details)
            check_out(self.driver, self.member_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
        except:
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise

    def test_invited_user(self):
       try:
           self.status_test = False
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
           # time.sleep(2)
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
           activity_complete(self.driver, self.invited_details)
           check_out(self.driver, self.invited_details)
           self.status_test = True
           statusOftest(self.status_test, self.driver)
       except:
           self.status_test = False
           statusOftest(self.status_test, self.driver)
           raise

    def test_invited_autofetch(self):

        try:
            self.status_test = False
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
            activity_complete(self.driver, self.invited_details)
            check_out(self.driver, self.invited_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
        except:
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise

    def test_general_activity_member(self):

       try:
           el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView")))
           el.click()
           # driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView').click()
           #time.sleep(0.05)
           setting_contact_member(self.driver)
           # time.sleep(2)
           FLEP_auto_fetch_member(self.driver, self.member_details)
           time.sleep(0.5)
           emergency_details_autofetch(self.driver, self.member_details)
           unique_id_autofetch(self.driver, self.member_details['unique_id'])
           gender_Screen(self.driver)
           time.sleep(1)
           # time.sleep(3)
           #general_activity_dropdown(self.driver)
           self.driver.find_element_by_xpath(
               '	(//android.view.ViewGroup[@content-desc="dropdownFormComponentField"])[1]').click()
           time.sleep(2)
           self.driver.find_element_by_xpath(
               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
           time.sleep(2)
           self.driver.find_element_by_xpath(
               '(//android.view.ViewGroup[@content-desc="dropdownFormComponentField"])[2]').click()
           time.sleep(3)
           self.driver.find_element_by_xpath(
               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup[1]').click()

           # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
           # time.sleep(1)
           self.driver.find_element_by_accessibility_id('nextButton').click()
           # time.sleep(3)
           cameraretake(self.driver)
           # time.sleep(2)
           activity_complete(self.driver, self.member_details)
           # time.sleep(2)
           check_out(self.driver, self.member_details)
           self.status_test = True
           statusOftest(self.status_test, self.driver)
           assert True
       except :
            print("exception")
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise

    def test_general_activity_walkin(self):

        try:
            useraction = TouchAction(self.driver)
            el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,                                                                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView")))
            el.click()
            time.sleep(0.5)
            contact = setting_contact(self.driver)
            time.sleep(1)
            FLEP_Screen(self.driver, self.walkin_details, contact)
            time.sleep(1)
            emergency_contact(self.driver, self.walkin_details)
            unique_id(self.driver, self.walkin_details['unique_id'])
            gender_Screen(self.driver)
            self.driver.hide_keyboard()
            time.sleep(3)
            #general_activity_dropdown(self.driver)
            
            self.driver.find_element_by_xpath('(//android.view.ViewGroup[@content-desc="dropdownFormComponentField"])[1]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath(
               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath(
               '(//android.view.ViewGroup[@content-desc="dropdownFormComponentField"])[2]').click()
            time.sleep(3)
            self.driver.find_element_by_xpath(
               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup[1]').click()
            
            self.driver.find_element_by_xpath('	(//android.view.ViewGroup[@content-desc="dropdownFormComponentField"])[1]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
            time.sleep(2)
            #useraction.press(x=211, y=166).move_to(x=375, y=166).release().perform()
            #useraction.tap(187, 196).perform()
            print('unable to select dropdown')
            self.driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button').click()
            time.sleep(1.1)

            time.sleep(2)
            self.driver.find_element_by_xpath('(//android.view.ViewGroup[@content-desc="dropdownFormComponentField"])[2]/android.view.ViewGroup').click()
            time.sleep(3)
            # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup[1]').click()
            # useraction.tap(x=270, y=196).perform()
            # useraction.tap(183, 313).perform()
            useraction.press(x=216, y=192).move_to(x=313, y=200).release().perform()
            # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()

            # time.sleep(1)
            time.sleep(2)
            next=WebDriverWait(self.driver, 3, poll_frequency=0.5).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID,'nextButton')))
            next.click()
            camera(self.driver)
            activity_complete(self.driver, self.walkin_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
        except:
            print("exception")
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise

    def test_general_activity_walkin_autofetch(self):
        try:
            el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView")))
            el.click()
            time.sleep(1)
            contact = setting_contact(self.driver)
            FLEP_auto_fetch_visitor(self.driver, self.walkin_details, contact)
            time.sleep(1)
            emergency_details_autofetch(self.driver, self.walkin_details)
            unique_id_autofetch(self.driver, self.walkin_details['unique_id'])
            gender_Screen(self.driver)
            general_activity_dropdown(self.driver)
            # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
            # time.sleep(1)
            next = WebDriverWait(self.driver, 3, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'nextButton')))
            next.click()
            cameraretake(self.driver)
            activity_complete(self.driver, self.walkin_details)
            #check_out(self.driver, self.walkin_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
        except:
            print("exception")
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise


    def test_walkin_details_offline(self):

        status="offline"
        walkin_visitor(self.driver,self.offline_walkin_details,status)
        assert True


    def test_request_meeting(self):
        #self.time.sleep(5)
        try:
            settings = WebDriverWait(self.driver, 15, poll_frequency=0.5).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "settingsButton")))
            settings.click()
            #time.sleep(3)
            self.driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="requestMeeting"]/android.view.ViewGroup/android.view.ViewGroup').click()

            Fname = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Your First Name")))
            Fname.send_keys('test_w')

            Lname = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Your Last Name")))
            Lname.send_keys('test_s')

            Phone = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Your Phone Number")))
            Phone.send_keys('2222200000')
            time.sleep(3)
            Meeting = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//android.view.ViewGroup[@content-desc="Meeting with?"]/android.widget.EditText')))
            Meeting.send_keys('Man')
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]').click()

            time11 = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, "dateTimePicker")))
            time11.click()

            c = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ID, "android:id/button1")))
            c.click()

            a = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Meeting Agenda")))
            a.send_keys('hi')
            self.driver.hide_keyboard()
            a = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                        "/ hierarchy / android.widget.FrameLayout / android.widget.LinearLayout / android.widget.FrameLayout / android.widget.FrameLayout / android.view.ViewGroup / android.view.ViewGroup / android.view.ViewGroup / android.widget.ScrollView / android.view.ViewGroup / android.widget.Switch")))
            a.click()

            a = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[10]")))
            a.click()
        except:
            print('Unable to request meeting')
            time.sleep(2)
            takeScreenshotError(self.driver)
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise

    def test_logout(self):
        logout(self.driver)




