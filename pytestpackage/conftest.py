import pytest
from utilities.Resources2 import *

@pytest.fixture(scope='module')
def data():
    start_server()
    data = settingup()
    yield data
@pytest.fixture(scope='module')
def driver(data):
    time.sleep(0.5)
    driver = launch_application(data['desired_capabilities'])
    #lists=[]
    #lists.append(driver)
    #lists.append(data)
    return driver
    """print("teardown")
    driver.close_app()
    driver.remove_app('com.veristerminal')
    driver.quit()"""
"""
@pytest.fixture
def driver(lists):
    driver=lists[0]
    return driver
"""

