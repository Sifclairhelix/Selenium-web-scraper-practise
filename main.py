import os
#webdriver needed for webbrowser
from selenium import webdriver

os.environ['PATH'] += r"C:/SeleniumDrivers"
#edge can also be used instead of Chrome
driver = webdriver.Chrome()