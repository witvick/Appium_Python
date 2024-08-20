from appium import webdriver
from typing import Any, Dict
from appium.options.android import UiAutomator2Options

# Define the desired capabilities
cap: Dict[str, Any] = {
    "platformName": "Android",
    "platformVersion": "14",  # Adjust to your device's Android version
    "automationName": "UiAutomator2",
    "deviceName": "R9WX705LKLH",
    "appPackage": "com.android.settings",  # Package name for Settings app
    "appActivity": "com.android.settings.Settings",  # Activity name for Settings app
    "noReset": True
}

# Initialize AppiumOptions
options = UiAutomator2Options()
options.load_capabilities(cap)

# URL for Appium server
url = 'http://127.0.0.1:4723'

driver = None  # Initialize driver variable

try:
    # Initialize the driver
    driver = webdriver.Remote(url, options=options)

    # Print confirmation message
    print("Settings app opened successfully.")

    # Add any additional test steps if needed here

finally:
    # End the session
    if driver is not None:
        driver.quit()
