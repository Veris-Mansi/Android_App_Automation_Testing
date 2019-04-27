import unittest
from python_testing.Resources2 import *
import pytest


class TestTerminal:
    lists=None
    @pytest.yield_fixture(scope='module')
    def lists(self):
        global lists
        print("====setup====")
        start_server()
        #time.sleep(2)
        lists = []
        data = {}
        data = settingup()
        driver = launch_application(data['desired_capabilities'])
        lists.append(driver)
        lists.append(data)
        yield lists
        print("====teardown====")
        driver = lists[0]
        driver.close_app()
        driver.remove_app('com.veristerminal')
        driver.quit()

    #@pytest.mark.order1
    def test_login(self,lists):
        time.sleep(2)
        self.driver = lists[0]
        login(self.driver)

    #@pytest.mark.order1
    def test_walkinvisitor(self,lists):
        driver = lists[0]
        mydata={}
        mydata = lists[1]
        walkin_details = mydata['walkin_details']
        user_action = TouchAction(driver)
        time.sleep(2)
        checkIn(driver)
        assert True
        time.sleep(3)
        setting_contact(driver)
        assert True
        time.sleep(7)
        driver.find_element_by_accessibility_id("Visitor").click()
        assert True
        time.sleep(3)
        camera(driver)
        assert True
        time.sleep(2)
        FLEP_Screen(driver, walkin_details)
        assert True
        time.sleep(3)
        Meeting_with_screen(driver)
        assert True
        time.sleep(1)
        unique_id(driver,walkin_details['unique_id'])
        assert True
        time.sleep(1)
        driver.execute_script('mobile:performEditorAction', {'action': 'done'})
        time.sleep(1)
        gender_Screen(driver)
        assert True
        time.sleep(3)
        Multi_select_screen(driver)
        assert True
        time.sleep(1)
        cardScanning(driver)
        time.sleep(1)
        single_dropdown_screen(driver)
        time.sleep(2)
        driver.find_element_by_accessibility_id('Address').send_keys(walkin_details['address'])
        driver.execute_script('mobile:performEditorAction', {'action': 'done'})
        time.sleep(2)
        emergency_contact(driver,walkin_details)
        time.sleep(2)
        rating_Screen(driver)
        time.sleep(1)
        driver.find_element_by_accessibility_id('nextButton').click()
        time.sleep(3)
        driver.find_element_by_accessibility_id('Mansi Test').click()
        time.sleep(3)
        NDA_screen(driver)
        time.sleep(3)
        user_action.tap(x=285, y=809).perform()
        time.sleep(2)
        user_action.tap(x=482, y=810).perform()
        time.sleep(3)
        date_and_time(driver)
        activity_complete(driver)
        assert True
        time.sleep(3)
        check_out(driver)
        return True

    @pytest.mark.order2
    def test_autofetch_user(self,lists):
        time.sleep(2)
        driver = lists[0]
        mydata = {}
        mydata = lists[1]
        walkin_details = mydata['walkin_details']
        time.sleep(1)
        checkIn(driver)
        time.sleep(5)
        contact_no=setting_contact(driver)
        time.sleep(3)
        driver.find_element_by_accessibility_id('Visitor').click()
        time.sleep(1)
        cameraretake(driver)
        time.sleep(2)
        FLEP_auto_fetch_visitor(driver, walkin_details,contact_no)
        time.sleep(3)
        Meeting_with_screen(driver)
        time.sleep(1)
        unique_id_autofetch(driver,walkin_details['unique_id'])
        time.sleep(2)
        gender_Screen(driver)
        time.sleep(2)
        Multi_select_screen(driver)
        time.sleep(3)
        Govt_Id_Retake(driver)
        time.sleep(3)
        single_dropdown_screen(driver)
        time.sleep(3)
        address = driver.find_element_by_xpath(
            '//android.view.ViewGroup[@content-desc="Address"]/android.widget.EditText')
        my_address = address.text

        print(my_address)
        assert my_address == walkin_details['address']
        time.sleep(3)
        emergency_details_autofetch(driver,walkin_details)
        time.sleep(3)
        rating_Screen(driver)
        driver.find_element_by_accessibility_id('nextButton').click()
        time.sleep(2)
        driver.find_element_by_accessibility_id('Mansi Test').click()
        time.sleep(2)
        NDA_screen(driver)
        user_action = TouchAction(driver)
        user_action.tap(x=285, y=809).perform()
        # driver.find_element_by_accessibility_id('printButton').click()
        time.sleep(2)
        user_action.tap(x=482, y=810).perform()
        time.sleep(2)
        date_and_time(driver)
        time.sleep(2)
        activity_complete(driver)
        time.sleep(3)
        check_out(driver)
        time.sleep(10)
    
    #@pytest.mark.order3
    def test_member_check_in(self,lists):
        driver = lists[0]
        mydata = {}
        mydata = lists[1]
        member_details = mydata['member_details']
        time.sleep(1)
        checkIn(driver)
        time.sleep(5)
        setting_contact_member(driver)
        time.sleep(3)
        cameraretake(driver)
        time.sleep(2)
        FLEP_auto_fetch_member(driver,member_details)
        time.sleep(2)
        emergency_details_autofetch(driver,member_details)
        time.sleep(1)
        unique_id_autofetch(driver,member_details['unique_id'])
        time.sleep(1)
        driver.find_element_by_accessibility_id("nextButton").click()
        time.sleep(1)
        NDA_screen(driver)
        time.sleep(2)
        Govt_Id_Retake(driver)
        user_action = TouchAction(driver)
        user_action.tap(x=285, y=809).perform()
        time.sleep(2)
        user_action.tap(x=482, y=810).perform()
        time.sleep(2)
        activity_complete(driver)

    #pytest.mark.order4
    def test_invited_user(driver, lists):

        driver = lists[0]
        mydata = {}
        mydata = lists[1]
        invited_details = mydata['invited_details']
        checkIn(driver)
        time.sleep(3)
        setting_contact_invite(driver)
        time.sleep(3)
        driver.find_element_by_accessibility_id('Invited').click()
        FLEP_auto_fetch_member(driver, invited_details)
        time.sleep(2)
        meeting = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Whom To Meet"]/android.widget.EditText')
        text = meeting.text
        if (len(text) > 0 and text == 'Mansi Sahu'):
            print("Meeting with test case passed")
            assert True
        else:
            print("Meeting with test case failed")
            assert False
        driver.find_element_by_accessibility_id('nextButton').click()
        time.sleep(2)
        activity_complete(driver)
"""
""" def test_invited_auto_fetch(driver, lists):

        driver = lists[0]
        mydata = {}
        mydata = lists[1]
        invited_details = mydata['invited_details']
        checkIn(driver)
        time.sleep(3)
        setting_contact_invite(driver)
        time.sleep(3)
        driver.find_element_by_accessibility_id('Invited').click()
        FLEP_auto_fetch_member(driver, invited_details)
        meeting = driver.find_element_by_xpath(
            '//android.view.ViewGroup[@content-desc="Whom To Meet"]/android.widget.EditText')
        text = meeting.text
        if (len(text) > 0 and text == 'Mansi Sahu'):
            assert True
            print("Meeting with test case passed")
        else:
            assert False
            print("Meeting with test case failed")
        driver.find_element_by_accessibility_id('nextButton').click()
        time.sleep(2)
        activity_complete(driver)
        time.sleep(1)

    def test_General_Activity_Member(driver,lists):

        driver = lists[0]
        mydata = {}
        mydata = lists[1]
        member_details = mydata['member_details']
        time.sleep(3)
        driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView').click()
        setting_contact_member(driver)
        time.sleep(2)
        FLEP_auto_fetch_member(driver, member_details)
        time.sleep(3)
        emergency_details_autofetch(driver,member_details)
        unique_id_autofetch(driver,member_details['unique_id'])
        time.sleep(3)
        gender_Screen(driver)
        time.sleep(3)
        driver.find_element_by_xpath(
            '(//android.view.ViewGroup[@content-desc="dropdownFormComponentField"])[1]/android.view.ViewGroup').click()
        time.sleep(1)
        driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '(//android.view.ViewGroup[@content-desc="dropdownFormComponentField"])[2]/android.view.ViewGroup').click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
        time.sleep(1)
        driver.find_element_by_accessibility_id('nextButton').click()
        time.sleep(3)
        cameraretake(driver)
        time.sleep(2)
        activity_complete(driver)
        time.sleep(2)

if __name__=='__main__':
    unittest.main()
