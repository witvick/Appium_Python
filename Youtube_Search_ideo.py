import time
from typing import Any, Dict
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.action_chains import ActionChains
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# Define the desired capabilities
cap: Dict[str, Any] = {
    "platformName": "Android",
    "platformVersion": "14",  # Adjust to your device's Android version
    "automationName": "UiAutomator2",
    "deviceName": "R9WX705LKLH",
    "appPackage": "com.google.android.youtube",
    "appActivity": "com.google.android.apps.youtube.app.WatchWhileActivity",
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

# got_it = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Got it"]')
#
# got_it.click()
# Allow = driver.find_element(by=AppiumBy.XPATH, value='// android.widget.Button[@text="Allow"]')

# Allow.click()
print("Permission granted")
# scroll=driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(5)')

search = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="Search"]')

search.click()
search2 = driver.find_element(by=AppiumBy.XPATH,
                              value='//android.widget.EditText[@resource-id="com.google.android.youtube:id/search_edit_text"]')
search2.click()
search2.send_keys("Mr Funracing")

driver.press_keycode(66)  # 66 is the key code for Enter

channel = driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Go to channel").instance(0)')

channel.click()
print("F")
videos_croup = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Videos"]')

videos_croup.click()
print("B")

videos_1 = driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="Oldest"]')

videos_1.click()
print("C")


# Find the element using UiSelector
element = driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().description("SOUNDCHECK Aprilia RS 125  Fly By – 2 minutes, 16 seconds – Go to channel – MrFunRacing - 5K views - 13 years ago – play video")'
)

# Perform long press action
actions = ActionChains(driver)
actions.click_and_hold(element).pause(5).release().perform()
print("Released perform")

download_1 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.LinearLayout[@content-desc="Download video"]')

download_1.click()
download_2 = driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(7)')

download_2.click()
time.sleep(800)
