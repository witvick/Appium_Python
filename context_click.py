import time
from typing import Any, Dict

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the desired capabilities
cap: Dict[str, Any] = {
    "platformName": "Android",
    "platformVersion": "14",
    "automationName": "UiAutomator2",
    "deviceName": "R9WX705LKLH",
    "appPackage": "com.android.gpstest",
    "appActivity": "com.android.gpstest.ui.MainActivity",
    "autoGrantPermissions": True
}

# Initialize AppiumOptions
options = UiAutomator2Options()
options.load_capabilities(cap)

# URL for Appium server
url = 'http://127.0.0.1:4723'
# Initialize the driver
driver = webdriver.Remote(url, options=options)
driver.implicitly_wait(10)
contexts = driver.contexts
print("Available contexts:", contexts)

# Wait for the TextView containing the link to be present
link_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[contains(@text,"CLOSE")]'))
)

link_element.click()

search = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="Open navigation drawer"]')
search.click()


search2 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Visit us on GitHub"]')
search2.click()

print(driver.contexts)
time.sleep(10)
# Python
webview = driver.contexts[1]
print(webview)
driver.switch_to.context(webview)

time.sleep(10)

scroll_end = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().flingToEnd(5)')

print("contect 1 clicked")

driver.switch_to.context('NATIVE_APP')

element=driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="Open navigation drawer"]')
element.click()

# Optional: Wait to observe the result of clicking the link
time.sleep(50)

# Close the driver
driver.quit()
