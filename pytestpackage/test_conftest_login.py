
import pytest
from utilities.Resources2 import *
import unittest

@pytest.mark.usefixtures("data","driver")
class TestLogin(unittest.TestCase):

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
