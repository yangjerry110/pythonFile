from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pdb
import json
import Leancloud

file = r'D:\wnmp\www\pythonFile\FIFA.json'

#driver = webdriver.Chrome("D:\pythonFile\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome()
driver.get('https://www.ol4vs.com')
html = driver.page_source    # 获取网页html
html_soup = BeautifulSoup(html,"html.parser")

try:
    dataInfo = driver.execute_script("var arr = [];var data = [];$('.item-player').each(function(){$(this).children().click();;var characteristicInfoImg = [];var characteristicInfoText = [];var dataInfo = {};var thisArr = {};var infoA = [];var infoB = [];var bodyInfo = $('.box-poslist').next().next().text();$('.list-xx-items .dib').each(function(){infoA.push($(this).html());});$('.list-xx-items .items-xx-val').each(function(){infoB.push($(this).html());});var thisInfoLength = infoA.length;for(var i=0;i<thisInfoLength;i++){thisArr[infoA[i]] = infoB[i];};$('.item-player-info-value .tz-item ').each(function(){characteristicInfoImg.push('https://www.ol4vs.com/'+$(this).find('img').attr('src'));characteristicInfoText.push($(this).find('span').html());});dataInfo['arr'] = thisArr;dataInfo['bodyInfo'] = bodyInfo;dataInfo['fancy_skill'] = $('.box-hsjq-val').attr('class').split(' ')[2];dataInfo['characteristicInfoImg'] = characteristicInfoImg;dataInfo['characteristicInfoText'] = characteristicInfoText;data.push(dataInfo)}); return data;")

    dataClassList = driver.execute_script("var data = [];$('.icon-sj').each(function(){var a = $(this).attr('class').split(' ')[1];data.push(a);}); return data")

    dataInfoIen = len(dataInfo)
    bodyInfoArray = []
    bodyAttributeArray = []
    fancySkillArray = []
    characteristicInfoImgArray = []
    characteristicInfoTextArray = [] 
    for i in range(dataInfoIen):
        if i%2 == 0:
            bodyAttributeArray.append(dataInfo[i]['arr'])
            bodyInfoArray.append(dataInfo[i]['bodyInfo'].replace(' ','').replace('\n',''))
            fancySkillArray.append(dataInfo[i]['fancy_skill'])
            characteristicInfoImgArray.append(dataInfo[i]['characteristicInfoImg'])
            characteristicInfoTextArray.append(dataInfo[i]['characteristicInfoText'])

except Exception as e:
    print(e)

    # tableHtml = html_soup.find_element_by_id('listPlayer')
    # table_rows = tableHtml.find_elements_by_tag_name('tr')
    # newsList = html_soup.find('table',{'class':'tb-team table table-hover table-striped'}).tbody.tr.td[4]
newsList = html_soup.find_all('table')

trList = []
for tr in newsList[0].tbody.find_all('tr'):
    try:
        tdList = []
        for td in tr.find_all('td'):
            showText = td.get_text().replace(' ','').replace('\n','')
            tdList.append(showText)
        del tdList[0]
        del tdList[0]
        del tdList[0]
        trList.append(tdList)
    except Exception:
        print('错误!')
    # print(trList)
    # pdb.set_trace() # 运行到这里会自动暂停

attributeList = html_soup.find_all('div',{'class':'box-poses-list'})
attributeListArray = []

for i in attributeList:
    try:
        attributeNameArray = []
        attributeValueArray = []
        attributeListSet = {}
        attributeNameSet = i.find_all('span',{'class':'label'})
        for name in attributeNameSet:
            attributeNameArray.append(name.get_text())
        attributeValueSet = i.find_all('span',{'class':'label-pos-val'})
        for value in attributeValueSet:
            attributeValueArray.append(value.get_text())
        
        arrayLen = len(attributeNameArray)
        for arrayNum in range(arrayLen):
            #print(attributeNameArray[arrayNum])
            attributeListSet[attributeNameArray[arrayNum]] = attributeValueArray[arrayNum]
        
        attributeListArray.append(attributeListSet)
    except Exception:
        print('错误!')

    # print(attributeListArray)
    # pdb.set_trace() # 运行到这里会自动暂停

nameClassList = html_soup.find_all('span',{'class':'item-player'})
nameArraySet = []
imgArraySet = []
nameClassListSet = []

for i in nameClassList:
    try:
        nameClassListSet.append(i)
    except Exception:
        print('错误!')

nameClassListSetLen = len(nameClassListSet)
for i in range(nameClassListSetLen):
    try:
        if i%2 == 0:
            imgArraySet.append('https://www.ol4vs.com/'+nameClassListSet[i].a.img.get('src'))
        else:
            nameArraySet.append(nameClassListSet[i].a.get_text())
    except Exception:
        print('错误!')
    # print(imgArraySet)
    # print(nameArraySet)
    # pdb.set_trace() # 运行到这里会自动暂停

itemArrayset = []
itemLen = len(trList)
for i in range(itemLen):
    try:
        itemSet = {}
        itemSet['country'] = trList[i][0] #国籍
        itemSet['ability_value'] = trList[i][1] #能力值
        itemSet['salary'] = trList[i][2] #薪水
        itemSet['name'] = nameArraySet[i] #名字
        itemSet['portrait'] = imgArraySet[i] #头像
        itemSet['attribute'] = json.dumps(attributeListArray[i]) #属性
        itemSet['body_attribute'] = json.dumps(bodyAttributeArray[i]) #详情属性
        itemSet['body_info'] = bodyInfoArray[i] #详情，身高，体重等等
        itemSet['class_name'] = dataClassList[i]
        itemSet['fancy_skill'] = fancySkillArray[i]
        itemSet['characteristic_img'] = characteristicInfoImgArray[i]
        itemSet['characteristic_text'] = characteristicInfoTextArray[i]
        #saveData = json.dumps(itemSet)
        #Leancloud.insertData(itemSet)
        print(itemSet)
    except Exception as e:
        print(e)
    itemArrayset.append(itemSet)

for i in range(2):
    driver.execute_script("$('.active').next().children().click()")

    html = driver.execute_script("return document.documentElement.outerHTML")
    html_soup = BeautifulSoup(html, "html.parser")

    try:
        dataInfo = driver.execute_script("var arr = [];var data = [];$('.item-player').each(function(){$(this).children().click();;var characteristicInfoImg = [];var characteristicInfoText = [];var dataInfo = {};var thisArr = {};var infoA = [];var infoB = [];var bodyInfo = $('.box-poslist').next().next().text();$('.list-xx-items .dib').each(function(){infoA.push($(this).html());});$('.list-xx-items .items-xx-val').each(function(){infoB.push($(this).html());});var thisInfoLength = infoA.length;for(var i=0;i<thisInfoLength;i++){thisArr[infoA[i]] = infoB[i];};$('.item-player-info-value .tz-item ').each(function(){characteristicInfoImg.push('https://www.ol4vs.com/'+$(this).find('img').attr('src'));characteristicInfoText.push($(this).find('span').html());});dataInfo['arr'] = thisArr;dataInfo['bodyInfo'] = bodyInfo;dataInfo['fancy_skill'] = $('.box-hsjq-val').attr('class').split(' ')[2];dataInfo['characteristicInfoImg'] = characteristicInfoImg;dataInfo['characteristicInfoText'] = characteristicInfoText;data.push(dataInfo)}); return data;")

        dataClassList = driver.execute_script("var data = [];$('.icon-sj').each(function(){var a = $(this).attr('class').split(' ')[1];data.push(a);}); return data")
    except Exception:
        print('错误!')
        
    dataInfoIen = len(dataInfo)
    bodyInfoArray = []
    bodyAttributeArray = []
    fancySkillArray = []
    characteristicInfoImgArray = []
    characteristicInfoTextArray = [] 
    for i in range(dataInfoIen):
        try:
            if i%2 == 0:
                bodyAttributeArray.append(dataInfo[i]['arr'])
                bodyInfoArray.append(dataInfo[i]['bodyInfo'].replace(' ','').replace('\n',''))
                fancySkillArray.append(dataInfo[i]['fancy_skill'])
                characteristicInfoImgArray.append(dataInfo[i]['characteristicInfoImg'])
                characteristicInfoTextArray.append(dataInfo[i]['characteristicInfoText'])
        except Exception:
            print('错误!')

        # tableHtml = html_soup.find_element_by_id('listPlayer')
        # table_rows = tableHtml.find_elements_by_tag_name('tr')
        # newsList = html_soup.find('table',{'class':'tb-team table table-hover table-striped'}).tbody.tr.td[4]
    newsList = html_soup.find_all('table')

    trList = []
    for tr in newsList[0].tbody.find_all('tr'):
        try:
            tdList = []
            for td in tr.find_all('td'):
                showText = td.get_text().replace(' ','').replace('\n','')
                tdList.append(showText)
            del tdList[0]
            del tdList[0]
            del tdList[0]
            trList.append(tdList)
        except Exception:
            print('错误!')
        # print(trList)
        # pdb.set_trace() # 运行到这里会自动暂停

    attributeList = html_soup.find_all('div',{'class':'box-poses-list'})
    attributeListArray = []

    for i in attributeList:
        try:
            attributeNameArray = []
            attributeValueArray = []
            attributeListSet = {}
            attributeNameSet = i.find_all('span',{'class':'label'})
            for name in attributeNameSet:
                attributeNameArray.append(name.get_text())
            attributeValueSet = i.find_all('span',{'class':'label-pos-val'})
            for value in attributeValueSet:
                attributeValueArray.append(value.get_text())
            
            arrayLen = len(attributeNameArray)
            for arrayNum in range(arrayLen):
                #print(attributeNameArray[arrayNum])
                attributeListSet[attributeNameArray[arrayNum]] = attributeValueArray[arrayNum]
            
            attributeListArray.append(attributeListSet)
        except Exception:
            print('错误!')
        
        # print(attributeListArray)
        # pdb.set_trace() # 运行到这里会自动暂停

    nameClassList = html_soup.find_all('span',{'class':'item-player'})
    nameArraySet = []
    imgArraySet = []
    nameClassListSet = []

    for i in nameClassList:
        try:
            nameClassListSet.append(i)
        except Exception:
            print('错误!')

    nameClassListSetLen = len(nameClassListSet)
    for i in range(nameClassListSetLen):
        try:
            if i%2 == 0:
                imgArraySet.append('https://www.ol4vs.com/'+nameClassListSet[i].a.img.get('src'))
            else:
                nameArraySet.append(nameClassListSet[i].a.get_text())
        except Exception:
            print('错误!')

        # print(imgArraySet)
        # print(nameArraySet)
        # pdb.set_trace() # 运行到这里会自动暂停

    #itemArrayset = []
    itemLen = len(trList)
    for i in range(itemLen):
        try:
            itemSet = {}
            itemSet['country'] = trList[i][0] #国籍
            itemSet['ability_value'] = trList[i][1] #能力值
            itemSet['salary'] = trList[i][2] #薪水
            itemSet['name'] = nameArraySet[i] #名字
            itemSet['portrait'] = imgArraySet[i] #头像
            itemSet['attribute'] = json.dumps(attributeListArray[i]) #属性
            itemSet['body_attribute'] = json.dumps(bodyAttributeArray[i]) #详情属性
            itemSet['body_info'] = bodyInfoArray[i] #详情，身高，体重等等
            itemSet['class_name'] = dataClassList[i]
            itemSet['fancy_skill'] = fancySkillArray[i]
            itemSet['characteristic_img'] = characteristicInfoImgArray[i]
            itemSet['characteristic_text'] = characteristicInfoTextArray[i]
            #saveData = json.dumps(itemSet)
            #Leancloud.insertData(itemSet)
            # with open(file,'a+') as f:
            #     f.write(saveData)
            print(itemSet)
        except Exception:
            print('错误!')
        itemArrayset.append(itemSet)

            # attributeName = i.find('span',{'class':'label'}).get_text()
            # attributeValue = i.find('span',{'class':'label-pos-val'}).get_text()
            # print(attributeName)
            # print(attributeValue)

        # for row in range(1,10):
        #     # table_col = table_rows[row].find_elements_by_tag_name('td')
        #     # for col in range(1,6):
        #     #     showText = table_rows[row].find_elements_by_tag_name('td')[col].text.replace(' ','').replace('\n','')
        #     #     print(showText)
        #     showNengLiZhi = table_rows[row].find_elements_by_tag_name('td')[4].text

jsonSaveData = json.dumps(itemArrayset)
with open(file,'a+') as f:
    f.write(jsonSaveData)