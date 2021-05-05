import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome("C:\\Users\\BB\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_xpath("//input[@value='radio3']").click()
driver.find_element_by_xpath("//input[@id='autocomplete']").send_keys("Vinay Sharma")
driver.find_element_by_css_selector("input[id='checkBoxOption1']").click()
driver.find_element_by_xpath("//input[@id='checkBoxOption3']").click()
time.sleep(10)
driver.maximize_window()
driver.close()

