from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\\Users\\BB\\Downloads\\driver\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(8)
driver.find_element_by_css_selector("a[href*='shop']").click()
cards = driver.find_elements_by_css_selector(".card-title a")
i = -1
for card in cards:
    i = i + 1
    cardText = card.text
    print(cardText)

    if cardText == "Blackberry":
        i = i
        driver.find_elements_by_xpath("//div[@class='card-footer']/button")[i].click()
driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
# time.sleep(5)
# self.verifyLinkPresence("India")
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[type='submit']").click()
textMatch = driver.find_element_by_css_selector("[class*='alert-success']").text
assert ("Success! Thank you!" in textMatch)
print(textMatch)
driver.close()