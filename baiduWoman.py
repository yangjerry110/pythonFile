#!/usr/bin/python
# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import leancloudTest
import random

searchKeyWord = ['育儿','母婴','旅行','家居','二次元','漫画','健康','萌宠','婚姻','星座','奇闻趣事','娱乐','时尚']

driver=webdriver.Chrome()
driver.maximize_window()

driver.get('https://passport.baidu.com/v2/?login')
time.sleep(3)
driver.find_element_by_id("TANGRAM__PSP_3__footerULoginBtn").click()
driver.find_element_by_name("userName").clear()
time.sleep(3)
driver.find_element_by_name("userName").send_keys('17187786687')
driver.find_element_by_name("password").clear()
time.sleep(3)
driver.find_element_by_name("password").send_keys('Syxj1718778')
time.sleep(3)
driver.find_element_by_id("TANGRAM__PSP_3__submit").click()

driver.get('https://www.baidu.com')

for i in range(100000000000000):
    driver.find_element_by_name('wd').send_keys(random.choice(searchKeyWord))
    driver.find_element_by_id('su').click()
    time.sleep(3)
    driver.find_element_by_name('wd').clear()

