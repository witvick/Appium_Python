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
    "autoGrantPermissions": True,
    "chromedriverExecutable": r'C:\Users\MR.WICK\AppData\Roaming\npm\node_modules\appium-chromedriver\chromedriver\win\chromedriver.exe',
    'webviewConnectTimeout': '90000',
    "chromeOptions": {
        "w3c": False
    },
    "goog:chromeOptions": {
        "args": ["--disable-infobars"]
    }
}

# Initialize AppiumOptions
options = UiAutomator2Options()
options.load_capabilities(cap)

# URL for Appium server
url = 'http://127.0.0.1:4723'
# Initialize the driver
driver = webdriver.Remote(url, options=options)
driver.implicitly_wait(10)

try:
    # Print available contexts
    contexts = driver.contexts
    print("Available contexts:", contexts)

    # Wait for and click the "CLOSE" button
    link_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[contains(@text,"CLOSE")]'))
    )
    link_element.click()

    # Open navigation drawer and click the GitHub link
    search = driver.find_element(by=AppiumBy.XPATH,
                                 value='//android.widget.ImageButton[@content-desc="Open navigation drawer"]')
    search.click()

    search2 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Visit us on GitHub"]')
    search2.click()

    # Print available contexts again
    contexts = driver.contexts
    print("Contexts after clicking GitHub link:", contexts)

    # Add a wait to ensure the WebView is fully loaded
    time.sleep(20)  # Increase wait time if needed

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

            old_height = driver.execute_script("return document.body.scrollHeight;")
            print(f"New document height: {old_height}")
            time.sleep(10)
            # Scroll to the end of the WebView using JavaScript
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print("Scrolled to the end of the WebView")

            # Verify scrolling by checking the document height
            new_height = driver.execute_script("return document.body.scrollHeight;")
            print(f"New document height: {new_height}")

        except Exception as e:
            print(f"Error while switching to WebView context or performing actions: {e}")
    else:
        print(f"Context {webview_context} not found")

finally:
    # End the session
    if driver is not None:
        driver.quit()
