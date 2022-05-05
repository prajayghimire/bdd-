import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('lauch a chrome browser')
def lauchbrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:/Users/Admin/Desktop/chromedriver.exe")


@when('Open the trackify website')
def step_impl(context):
    context.driver.get("https://test.trackify.com.au/")
    time.sleep(5)


@then('verify the logo is present in the webiste')
def step_impl(context):
    x = context.driver.find_element(By.XPATH, "//body/div[3]/section[1]/div[1]/div[1]/div[1]/div[1]/img[1]").is_displayed()
    assert x is True



@then('Close the browser')
def close_browser(context):
    context.driver.close()

