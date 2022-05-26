from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Safari()

browser.get('https://docs.python.org/3/')
assert 'Documentation' in browser.title

elem = browser.find_element(By.NAME, 'q')  # Find the search box
elem.send_keys('class' + Keys.RETURN)
assert 'Search' in browser.title

browser.quit()
