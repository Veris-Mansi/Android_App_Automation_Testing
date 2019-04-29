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



