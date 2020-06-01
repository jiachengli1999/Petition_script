from selenium import webdriver
import time
import random
from random import randrange

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)
first_name = 'Mike'
last_name = 'Yagami'
email = 'mikeyagmai@gmail.com'
urls = ['https://www.change.org/p/black-lives-matter-activists-justice-for-tony-mcdade', 'https://www.change.org/p/gregg-abbott-justice-for-jennifer-jeffley']
for url in urls:
    driver.get(url)
    time.sleep(2)

    # enters data into fields
    inputElement = driver.find_element_by_id("firstName")
    inputElement.send_keys(first_name)

    inputElement = driver.find_element_by_id("lastName")
    inputElement.send_keys(last_name)

    inputElement = driver.find_element_by_id("email")
    inputElement.send_keys(email)

    driver.find_element_by_xpath('//button[normalize-space()="Sign this petition"]').click()
    # wait 5 seconds for web page to load
    time.sleep(5)
    driver.find_element_by_xpath("//button[normalize-space()='No, I'll share instead']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//button[normalize-space()='Send an email']").click()


time.sleep(5)
driver.quit()

