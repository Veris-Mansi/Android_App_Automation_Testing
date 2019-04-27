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

    def test_login(self):
        time.sleep(2)
        login(self.driver)

    def test_walkin(self):
        user_action = TouchAction(self.driver)
        checkIn(self.driver)
        setting_contact(self.driver)
        visitor=WebDriverWait(self.driver, 3, poll_frequency=0.5).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Visitor")))
        if(visitor.is_displayed()):
            assert True
            visitor.click()
        else:
            assert False
        camera(self.driver)