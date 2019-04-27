"""
If pytest will not find fixtures in class itself then it will check for the conf_test file
"""

import pytest
from utilities.Resources2 import *

@pytest.mark.usefixtures("data","driver","status_test")
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
        self.status=True

    def test_walkin(self):
        user_action = TouchAction(self.driver)
        checkIn(self.driver)
        contact=setting_contact(self.driver)
        visitor=WebDriverWait(self.driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Visitor")))
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
        self.driver.find_element_by_accessibility_id('nextButton').click()
        a=WebDriverWait(self.driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Mansi Test")))
        a.click()
        NDA_screen(self.driver)
        time.sleep(1)
        user_action.tap(x=285, y=809).perform()
        time.sleep(0.1)
        user_action.tap(x=482, y=810).perform()
        date_and_time(self.driver)
        activity_complete(self.driver)
        check_out(self.driver)

