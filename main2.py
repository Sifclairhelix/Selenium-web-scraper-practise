import os
# webdriver needed for webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"C:/SeleniumDrivers"
# edge can also be used instead of Chrome
driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
driver.implicitly_wait(8)

try:
    no_button = driver.find_element_by_class_name("at-cm-no-button")
    no_button.click()
except:
    print("no class name equal to that found")

sum1 = driver.find_element_by_id("sum1")
sum2 = driver.find_element_by_id("sum2")

sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
sum2.send_keys(20)

btn = driver.find_element_by_css_selector("button[onclick='return total()']")
btn.click()
