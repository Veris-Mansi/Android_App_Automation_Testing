import pytest
from utilities.Resources2 import *

@pytest.mark.usefixtures("data","driver")
class TestOFFLINE():

    @pytest.fixture(autouse=True)
    def classSetup(self,data,driver):
        self.driver=driver
        self.data=data
        self.walkin_details=data['walkin_details']
        self.member_details=data['member_details']
        self.invited_details=data['invited_details']
        self.offline_walkin_details = data['offline_walkin_details']

    def test_walkin_details_offline(self):

        offline_mode(self.driver)
        time.sleep(1)
        walkin_visitor(self.driver, self.offline_walkin_details)

    def test_autofetch_offline(self):
        autofetch_user(self.driver,self.offline_walkin_details)

    def test_lastcheckedin_autofetch(self):
        autofetch_user(self.driver,self.walkin_details)

    def test_autofetch_member(self):
        autofetch_user(self.driver,self.member_details)