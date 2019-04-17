from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
desired_cap={
  "app": "C:\\Users\\veris\\Downloads\\appium\\332.apk",
  "platformName": "Android",
  "deviceName": "RZ8M30B0LNZ"
}
#We can invoke our application in real device
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

driver.implicitly_wait(30)
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()

driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.support.v7.widget.LinearLayoutCompat/TextInputLayout[1]/android.widget.FrameLayout/android.widget.EditText')))

driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.support.v7.widget.LinearLayoutCompat/TextInputLayout[1]/android.widget.FrameLayout/android.widget.EditText').send_keys("V")