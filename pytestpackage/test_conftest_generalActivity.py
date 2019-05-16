import pytest
from utilities.Resources2 import *


@pytest.mark.usefixtures("data","driver")

class TestLogin():

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

    def test_general_activity_member(self):

        try:
            el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView")))
            el.click()
            # driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView').click()
            # time.sleep(0.05)
            setting_contact_member(self.driver)
            # time.sleep(2)
            FLEP_auto_fetch_member(self.driver, self.member_details)
            time.sleep(0.5)
            emergency_details_autofetch(self.driver, self.member_details)
            unique_id_autofetch(self.driver, self.member_details['unique_id'])
            gender_Screen(self.driver)
            time.sleep(1)
            # time.sleep(3)
            general_activity_dropdown(self.driver)

            next = WebDriverWait(self.driver, 3, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'nextButton')))
            next.click()

            # time.sleep(3)
            cameraretake(self.driver)
            # time.sleep(2)
            activity_complete(self.driver, self.member_details)
            # time.sleep(2)
            check_out(self.driver, self.member_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
            assert True
        except:
            print("exception")
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise

    def test_general_activity_walkin(self):

        try:
            useraction = TouchAction(self.driver)
            el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView")))
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
            general_activity_dropdown(self.driver)
            next = WebDriverWait(self.driver, 3, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'nextButton')))
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
            # check_out(self.driver, self.walkin_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
        except:
            print("exception")
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise
