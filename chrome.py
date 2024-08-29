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

    # Print available contexts again
    contexts = driver.contexts
    print("Contexts after clicking link:", contexts)

    # Add a wait to ensure the WebView is fully loaded
    time.sleep(10)

    # Determine the WebView context name
    webview_context = 'WEBVIEW_chrome'  # Ensure this matches your actual context name
    if webview_context in contexts:
        try:
            driver.switch_to.context(webview_context)
            print(f"Successfully switched to context: {webview_context}")

            # Print current context to confirm switch
            current_context = driver.current_context
            print(f"Current context after switch: {current_context}")

            time.sleep(10)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print("Scrolled to the end of the WebView")

            print("Scrolled to the end of the WebView")

        except Exception as e:
            print(f"Error while switching to WebView context or performing actions: {e}")
    else:
        print(f"Context {webview_context} not found")

    time.sleep(5)
    print("youtube Opened")


    time.sleep(5)



finally:
    # End the session
    if driver is not None:
        driver.quit()
