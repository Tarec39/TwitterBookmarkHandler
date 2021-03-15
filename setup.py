from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_dir = "./chrome/chromedriver.exe"
driver = webdriver.Chrome(driver_dir)
driver.get('https://google.com/')