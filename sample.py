from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time
import pprint

#global
driver = webdriver.Chrome(os.environ['DRIVER_DIR'])

def accessToTwitter():
    print("Start Access")
    driver.get('https://twitter.com/login')
    time.sleep(2)
    print("Accessed to Twitter")
    return login()

def login():
    print("Try to Login")
    input_id = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
    input_pass = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
    btn_login = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]')
    elements = {input_id : os.environ['USER_ID'], input_pass : os.environ['USER_PASS']}
    # pprint.pprint(elements)
    for key, value in elements:
        key.click(value)
        time.sleep(1)
        key.send_keys(value)
    time.sleep(1)
    btn_login.click()
    time.sleep(2)
    print("Logined")

def accessToBookmark():
    driver.get('https://twitter.com/i/bookmarks')
    time.sleep(2)

def scroll_down():
    height = driver.execute_script("return document.body.scrollHeight")
    i=0
    while True:
        for x in range(i,height):
            driver.execute_script("window.scrollTo(0, "+str(x*4)+");")
            i+=1
        height = driver.execute_script("return document.body.scrollHeight")

accessToTwitter()
time.sleep(3)
driver.quit()
