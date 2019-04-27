import pytest

from python_testing.Files.Resources import *


@pytest.fixture(scope='module')
def lists():
    print("====setup====")
    start_server()
    time.sleep(2)
    lists=[]
    data={}
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

def test_login(lists):

    time.sleep(3)
    driver = lists[0]
    login(driver)


def test_walkinvisitor(lists):

    driver=lists[0]
    mydata=lists[1]
    walkin_details=mydata['walkin_details']
    user_action=TouchAction(driver)
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
    FLEP_Screen(driver,walkin_details)
    assert True
    time.sleep(3)
    Meeting_with_screen(driver)
    assert True
    time.sleep(1)
    unique_id(driver)
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
    driver.find_element_by_accessibility_id('Address').send_keys('JMD')
    driver.execute_script('mobile:performEditorAction', {'action': 'done'})
    time.sleep(2)
    emergency_contact(driver)
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
    user_action.tap(x=482,y=810).perform()
    time.sleep(3)
    date_and_time(driver)
    activity_complete(driver)

    assert True
    time.sleep(3)

    #user_action.tap(x=450, y=906).perform()
    #time.sleep(10)

    check_out(driver)
    return True
