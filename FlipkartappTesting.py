import time
from appium import  webdriver

desired_capabilities={
  "app": "C:\\Users\\veris\\Downloads\\flipkart_apk\\Flipkart Online Shopping App_v6.12_apkpure.com (1).apk",
  "platformName": "Android",
  "deviceName": "fc378d12",
}

#Creating the driver instance
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_capabilities)

driver.implicitly_wait(40)
#Interacting with textbox
driver.find_element_by_id("com.flipkart.android:id/btn_skip").click()
#driver.find_element_by_accessibility_id("Search on flipkart").click()
#driver.find_element_by_accessibility_id("Search grocery products in Supermart").send_keys("iphone")

driver.find_element_by_accessibility_id("Drawer").click()
#time.sleep(10)
driver.find_element_by_id("com.flipkart.android:id/flyout_parent_title").click()

driver.find_element_by_id("com.flipkart.android:id/title").click()
driver.find_element_by_id("com.flipkart.android:id/tv_card_view_holder").click()
driver.find_element_by_id("com.flipkart.android:id/not_now_button").click()

price = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[4]").get_attribute("text")

print("The first mobile price value is "+price)