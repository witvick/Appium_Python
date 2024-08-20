from appium import webdriver
from typing import Any,Dict

from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
from appium.options.common import AppiumOptions


# Define the desired capabilities
cap:Dict[str,Any]={
  "platformName": "Android",
  "appium:platformVersion": "14",
  "appium:automationName": "UiAutomator2",
  "appium:deviceName": "R9WX705LKLH",
  "appium:appPackage": "com.sand.airmirror",
  "appium:appActivity": "com.sand.airmirror.ui.splash.SplashActivity",
  "noReset": "true"
}

url='http://127.0.0.1:4723'

# Initialize AppiumOptions
options = UiAutomator2Options()
options.load_capabilities(cap)

try:
    driver = webdriver.Remote(url, options=options)
    # The script will simply start the app and then stop
    print("App launched successfully.")
    # Add a wait or some logic if needed
except:
    None