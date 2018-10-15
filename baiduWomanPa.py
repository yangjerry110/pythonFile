#!/usr/bin/python
# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import leancloudTest

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

for i in range(100):
    driver.get('https://www.baidu.com')
    driver.find_element_by_class_name('animate-arrow').click()

    for i in range(1000):
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        #js = "var q=document.body.scrollTop=100000"
        #driver.execute_script(js)
        time.sleep(0.1)

    html = driver.execute_script("return document.documentElement.outerHTML")
    bsObj = BeautifulSoup(html, "html.parser")
    newsList = bsObj.find_all('div',{'class':'s-news-list-wrapper'})
    for i in newsList:
        try:
            title = i.find('div',{'class':'s-text-content'}).h2.a.get_text()
            author = i.find('span',{'class':'src-net'}).a.get_text()
            img_url = i.find('li',{'class':'item-img-wrap'}).a.img.get('src')
            thisHref = i.find('div',{'class':'s-text-content'}).h2.a.get('href')
            driver.get(thisHref)
            thisHtml = driver.page_source
            thisObj = BeautifulSoup(thisHtml, "html.parser")
            content = thisObj.find('div',{'class':'article-content'}).get_text()
            leancloudTest.insertDataForBaidu(title,author,img_url,content,thisHref,2)
            print('插入正确')
        except Exception:
            print('错误!')

driver.quit()
