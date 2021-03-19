from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time
import pprint
import logging

#global
driver = webdriver.Chrome(os.environ['DRIVER_DIR'])
driver.set_window_size(960 ,540)

# logging.basicConfig(level=logging.DEBUG)

def accessToTwitter():
    logging.debug('アクセス中...')
    driver.get('https://twitter.com/login')
    time.sleep(2)
    logging.debug('アクセス成功')
    return login()

def login():
    logging.debug('ログイン中...')
    input_id = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
    input_pass = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
    btn_login = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]')
    # elements = {input_id : os.environ['USER_ID'], input_pass : os.environ['USER_PASS']}
    # pprint.pprint(elements)
    # for key, value in elements:
    #     key.click(value)
    #     time.sleep(1)
    #     key.send_keys(value)
    input_id.click()
    time.sleep(1)
    input_id.send_keys(os.environ['USER_ID'])
    time.sleep(1)
    input_pass.click()
    time.sleep(1)
    input_pass.send_keys(os.environ['USER_PASS'])
    btn_login.click()
    time.sleep(2)
    logging.debug('ログイン成功')
    return accessToBookmark()

def accessToBookmark():
    logging.debug('ブックマークにアクセス中...')
    driver.get('https://twitter.com/i/bookmarks')
    time.sleep(2)
    logging.debug('ブックマークにアクセス成功')
    return scroll_down()

def scroll_down():
    logging.debug('スクロール実行中...')
    height = driver.execute_script("return document.body.scrollHeight")
    i=0
    while True:
        for x in range(i, height):
            driver.execute_script("window.scrollTo(0, "+str(x*3)+");")
            i+=1
        print(i)
        new_height = driver.execute_script("return document.body.scrollHeight")
        height = int(new_height / 3)
        pprint.pprint(height)
        print('---------------------------')
        if i == height:
            break
            

    logging.debug('スクロールを完了しました。')
    return load_page_source()

def load_page_source():
    html = driver.page_source
    driver.quit()
# def post_counter():
#     bookmarks = driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div')
#     print(len(bookmarks))
# //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]
# /html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]
accessToTwitter()
time.sleep(3)

