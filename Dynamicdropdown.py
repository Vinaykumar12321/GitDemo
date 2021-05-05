import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome("C:\\Users\\BB\\Downloads\\driver\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(5)
Countries = driver.find_elements_by_xpath("//ul[@id='ui-id-1']/li[2]/a")
print(len(Countries))
for country in Countries:
    if country.text == "India":
        country.click()
        break
print(driver.find_element_by_id("autosuggest").text)
assert driver.find_element_by_id("autosuggest").get_attribute("value") == "India"
