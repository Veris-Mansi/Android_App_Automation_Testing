import unittest
from pytestpackage.test_conftest_login import TestLogin
from pytestpackage.test_conftest_walkin import TestWalkIn
from pytestpackage.test_conftest_Invites import TestInvites


tc1=unittest.TestLoader().loadTestsFromTestCase(TestLogin)
tc2=unittest.TestLoader().loadTestsFromTestCase(TestWalkIn)
tc3=unittest.TestLoader().loadTestsFromTestCase(TestInvites)

smokeTest=unittest.TestSuite([tc1,tc2,tc3])
unittest.TextTestRunner(verbosity=2).run(smokeTest)