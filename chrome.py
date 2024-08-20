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

}

# Initialize AppiumOptions
options = UiAutomator2Options()
options.load_capabilities(cap)

# URL for Appium server
url = 'http://127.0.0.1:4723'
# Initialize the driver
driver = webdriver.Remote(url, options=options)

try:

    chrome = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Chrome')
    time.sleep(5)
    chrome.click()
    print("Chrome App Opened.")
    time.sleep(5)
    search_box=driver.find_element(by=AppiumBy.ID,value='com.android.chrome:id/search_box_text')
    time.sleep(5)
    search_box.click()
    time.sleep(5)
    url_box = driver.find_element(by=AppiumBy.ID, value='com.android.chrome:id/url_bar')
    url_box.send_keys("youtube")
    time.sleep(5)
    time.sleep(5)
    driver.press_keycode(66)  # 66 is the key code for Enter

    time.sleep(5)
    print("youtube Opened")



    time.sleep(5)




    # Print confirmation message



    # Add any additional test steps if needed here

finally:
    # End the session
    if driver is not None:
        driver.quit()
