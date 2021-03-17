from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

driver = webdriver.Chrome(os.environ['DRIVER_DIR'])
driver.get('https://twitter.com/login')

time.sleep(2)

input_id = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
input_pass = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')

btn_login = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]')

time.sleep(1)

input_id.click()
time.sleep(1)
input_id.send_keys(os.environ['USER_ID'])

time.sleep(1)

input_pass.click()
time.sleep(1)
input_pass.send_keys(os.environ['USER_PASS'])

time.sleep(1)

btn_login.click()

time.sleep(2)

bookmark = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[5]/div')

bookmark.click()
time.sleep(3)

#ボツ
# def scroll_down():
#         height = driver.execute_script("return document.body.scrollHeight")
#     while True:
#         for x in range(1,height):
#             driver.execute_script("window.scrollTo(0, "+str(x*2)+");")
#             height = driver.execute_script("return document.body.scrollHeight")
#         break

def scroll_down_2():
    SCROLL_PAUSE_TIME = 2
    last_height = driver.execute_script("return document.body.scrollHeight")
    x = 0
    while True:
        # Scroll down to bottom
        x = x + 1
        driver.execute_script("window.scrollTo(0, "+str(x*4)+");")
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print('Reached')
            break
#ボツ
# def scroll_down_3():
#     i = 1
#     height = driver.excute_script("return document.body.scrollHeight")
#     while True:
#         for x in range(i, height):
#             driver.execute_script("window.scrollTo(0, "+str(x*2)+");")
#             i = i*2
#         height = driver.excute_script("return document.body.scrollHeight")

scroll_down_2()

time.sleep(3)
driver.quit()