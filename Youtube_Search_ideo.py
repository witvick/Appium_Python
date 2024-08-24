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
    time.sleep(5)
    search = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.ImageView[@content-desc="Search"]')
    time.sleep(5)
    search.click()
    search2 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="com.google.android.youtube:id/search_edit_text"]')
    search2.click()
    search2.send_keys("Mr Funracing")

    driver.press_keycode(66)  # 66 is the key code for Enter
    time.sleep(5)
    channel = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().description("Go to channel").instance(0)')
    time.sleep(5)
    channel.click()
    print("F")
    videos_croup = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="VIDEOS"]')
    time.sleep(10)
    videos_croup.click()
    print("B")

    videos_1 = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="Oldest"]')
    time.sleep(5)
    videos_1.click()
    print("C")
    time.sleep(5)

    channel_ideo = driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("SOUNDCHECK Aprilia RS 125  Fly By – 2 minutes, 16 seconds – Go to channel – MrFunRacing - 5K views - 13 years ago – play video")')
    time.sleep(10)
    channel_ideo.click()

    time.sleep(100)





finally:
    None
