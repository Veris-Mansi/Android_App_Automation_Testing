import pytest
from utilities.Resources2 import *
import unittest

@pytest.mark.usefixtures("data","driver")

class TestInvites(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,data,driver):
        self.driver=driver
        self.data=data
        self.walkin_details=data['walkin_details']
        self.member_details=data['member_details']
        self.invited_details=data['invited_details']

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
