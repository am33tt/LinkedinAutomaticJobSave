import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions

options = ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://linkedin.com')

username = driver.find_element(By.XPATH, value='//*[@id="session_key"]')
password = driver.find_element(By.XPATH, value='//*[@id="session_password"]')
username.send_keys(os.environ.get('LINKEDIN_USERNAME'))
password.send_keys(os.environ.get('LINKEDIN_PASSWORD'))
button = driver.find_element(By.XPATH, value='//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
button.send_keys(Keys.ENTER)

time.sleep(20)

search = driver.find_element(By.XPATH, value='//*[@id="global-nav-typeahead"]/input')
search.click()
search.send_keys('Python Developer')
search.send_keys(Keys.ENTER)

time.sleep(7)
select_jobs = driver.find_element(By.XPATH, value='//*[@id="search-reusables__filters-bar"]/ul/li[1]/button')
select_jobs.click()

time.sleep(7)

easy_apply = driver.find_element(By.CSS_SELECTOR, value='.search-reusables__filter-binary-toggle')
easy_apply.click()

time.sleep(7)
jobs = driver.find_elements(By.CSS_SELECTOR, value='.job-card-container--clickable')

for items in jobs:
    time.sleep(7)
    items.click()
    time.sleep(5)
    save_button = driver.find_element(By.CSS_SELECTOR, value='.jobs-save-button')
    save_button.click()
    time.sleep(3)
    follow_button = driver.find_element(By.CSS_SELECTOR, value='.jobs-company__box button')
    follow_button.click()


