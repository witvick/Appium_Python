from appium import webdriver
from typing import Any, Dict
from appium.options.android import UiAutomator2Options
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Keys

# Define the desired capabilities
cap: Dict[str, Any] = {
    "platformName": "Android",
    "platformVersion": "14",  # Adjust to your device's Android version
    "automationName": "UiAutomator2",
    "deviceName": "R9WX705LKLH",
    "appPackage": "com.google.android.youtube",
    "appActivity": "com.google.android.apps.youtube.app.WatchWhileActivity"

}

# Initialize AppiumOptions
options = UiAutomator2Options()
options.load_capabilities(cap)

# URL for Appium server
url = 'http://127.0.0.1:4723'
# Initialize the driver
driver = webdriver.Remote(url, options=options)

try:

    got_it = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Got it"]')
    time.sleep(5)
    got_it.click()
    Allow=driver.find_element(by=AppiumBy.XPATH, value='// android.widget.Button[@text="Allow"]')
    time.sleep(5)
    Allow.click()
    print("Permission granted")
    #scroll=driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(5)')
    time.sleep(10)
    scroll_end = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().flingToEnd(5)')
    time.sleep(10)
    print("Fling 1 Completed")
    time.sleep(10)
    scroll_beg = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().flingToBeginning(4)')
    time.sleep(10)
    print("Fling 2 Completed")
    time.sleep(5)




finally:
    # End the session
    if driver is not None:
        driver.quit()
