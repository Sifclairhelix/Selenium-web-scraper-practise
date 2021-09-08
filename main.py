import os
#webdriver needed for webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"C:/SeleniumDrivers"
#edge can also be used instead of Chrome
driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")
driver.implicitly_wait(8)
my_element = driver.find_element_by_id("downloadButton")
my_element.click()


# progcomplete_element = driver.find_element_by_class_name("progress-label")
# print(f"{progcomplete_element.text == 'Completed!'}")


WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),# Element filteration
        'Complete!'#the expected text
        
    )
)
#testing the implicity wait function
#my_second_element = driver.find_element_by_id('chocolate')