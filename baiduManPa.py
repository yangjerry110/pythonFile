#!/usr/bin/python
# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import leancloudTest
import random

searchKeyWord = ['旅行','星座','二次元','房产','数码','汽车','军事航空','体育','直播','美女','时尚','奇闻趣事','娱乐八卦','男性穿衣搭配']
#searchKeyWord = ['婚姻']
driver=webdriver.Chrome()
driver.maximize_window()

driver.get('https://passport.baidu.com/v2/?login')
time.sleep(3)
driver.find_element_by_id("TANGRAM__PSP_3__footerULoginBtn").click()
driver.find_element_by_name("userName").clear()
time.sleep(3)
driver.find_element_by_name("userName").send_keys('13301733871')
driver.find_element_by_name("password").clear()
time.sleep(3)
driver.find_element_by_name("password").send_keys('Mlsq1718778')
time.sleep(3)
driver.find_element_by_id("TANGRAM__PSP_3__submit").click()

for y in range(2):
    #driver.get('https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word='+x)
    html = driver.page_source
    for x in searchKeyWord:
        thisPageNum = y*10
        driver.get('https://www.baidu.com/s?ie=utf-8&cl=2&rtt=1&bsst=1&tn=news&word='+x+'&x_bfe_rqs=03E80&x_bfe_tjscore=0.002456&tngroupname=organic_news&pn=%s' % thisPageNum)
        html = driver.page_source
        #html = driver.execute_script("return document.documentElement.outerHTML")
        bsObj = BeautifulSoup(html, "html.parser")
        newsList = bsObj.find_all('div',{'class':'result'})
        for i in newsList:
            try:
                title = i.h3.a.get_text().replace(" ",'').replace('\n','')
                #descrtiption = i.find('div',{'class':'c-span-last'}).get('text').replace(' ','')
                #author = '百家号'
                img_url = i.find('div',{'class':'c-span6'}).a.img.get('src')
                thisHref = i.h3.a.get('href')
                driver.get(thisHref)
                thisHtml = driver.page_source
                thisObj = BeautifulSoup(thisHtml, "html.parser")
                content = thisObj.find('div',{'class':'article-content'}).get_text()
                author = thisObj.find('p',{'class':'author-name'}).get_text()
                leancloudTest.insertDataForBaidu(title,author,img_url,content,thisHref,1)
                print('正确')
            except Exception:
                print('错误!')
