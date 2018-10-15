from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pdb

#driver = webdriver.Chrome("D:\pythonFile\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome()
driver.get('https://www.ol4vs.com')
html = driver.page_source    # 获取网页html
html_soup = BeautifulSoup(html,"html.parser")

dataInfo = driver.execute_script("var arr = [];var dataInfo = {};var data = [];$('.item-player').each(function(){$(this).children().click();var thisArr = {};var infoA = [];var infoB = [];var bodyInfo = $('.box-poslist').next().next().text();$('.list-xx-items .dib').each(function(){infoA.push($(this).html());});$('.list-xx-items .items-xx-val').each(function(){infoB.push($(this).html());});var thisInfoLength = infoA.length;for(var i=0;i<thisInfoLength;i++){thisArr[infoA[i]] = infoB[i];}dataInfo['arr'] = thisArr;dataInfo['bodyInfo'] = bodyInfo;data.push(dataInfo)}); return data;")

dataInfoIen = len(dataInfo)
bodyInfoArray = []
bodyAttributeArray = []
for i in range(dataInfoIen):
    if i%2 == 0:
        bodyAttributeArray.append(dataInfo[i]['arr'])
        bodyInfoArray.append(dataInfo[i]['bodyInfo'].replace(' ','').replace('\n',''))

#pdb.set_trace()

# tableHtml = html_soup.find_element_by_id('listPlayer')
# table_rows = tableHtml.find_elements_by_tag_name('tr')
# newsList = html_soup.find('table',{'class':'tb-team table table-hover table-striped'}).tbody.tr.td[4]
newsList = html_soup.find_all('table')

trList = []
for tr in newsList[0].tbody.find_all('tr'):
    tdList = []
    for td in tr.find_all('td'):
        showText = td.get_text().replace(' ','').replace('\n','')
        tdList.append(showText)
    del tdList[0]
    del tdList[0]
    del tdList[0]
    trList.append(tdList)
# print(trList)
# pdb.set_trace() # 运行到这里会自动暂停

attributeList = html_soup.find_all('div',{'class':'box-poses-list'})
attributeListArray = []

for i in attributeList:
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

# print(attributeListArray)
# pdb.set_trace() # 运行到这里会自动暂停

nameClassList = html_soup.find_all('span',{'class':'item-player'})
nameArraySet = []
imgArraySet = []
nameClassListSet = []

for i in nameClassList:
    nameClassListSet.append(i)

nameClassListSetLen = len(nameClassListSet)
for i in range(nameClassListSetLen):
    if i%2 == 0:
        imgArraySet.append('https://www.ol4vs.com/'+nameClassListSet[i].a.img.get('src'))
    else:
        nameArraySet.append(nameClassListSet[i].a.get_text())

# print(imgArraySet)
# print(nameArraySet)
# pdb.set_trace() # 运行到这里会自动暂停

itemArrayset = []
itemLen = len(trList)
for i in range(itemLen):
    itemSet = {}
    itemSet['country'] = trList[i][0] #国籍
    itemSet['ability_value'] = trList[i][1] #能力值
    itemSet['salary'] = trList[i][2] #薪水
    itemSet['name'] = nameArraySet[i] #名字
    itemSet['salary'] = imgArraySet[i] #头像
    itemSet['attribute'] = attributeListArray[i] #属性
    itemSet['bodyAttributeArray'] = bodyAttributeArray[i]
    itemSet['bodyInfoArray'] = bodyInfoArray[i]
    print(itemSet)
    itemArrayset.append(itemSet)

for i in range(2):
    driver.execute_script("$('.active').next().children().click()")

    html = driver.execute_script("return document.documentElement.outerHTML")
    html_soup = BeautifulSoup(html, "html.parser")

    ataInfo = driver.execute_script("var arr = [];var dataInfo = {};var data = [];$('.item-player').each(function(){$(this).children().click();var thisArr = {};var infoA = [];var infoB = [];var bodyInfo = $('.box-poslist').next().next().text();$('.list-xx-items .dib').each(function(){infoA.push($(this).html());});$('.list-xx-items .items-xx-val').each(function(){infoB.push($(this).html());});var thisInfoLength = infoA.length;for(var i=0;i<thisInfoLength;i++){thisArr[infoA[i]] = infoB[i];}dataInfo['arr'] = thisArr;dataInfo['bodyInfo'] = bodyInfo;data.push(dataInfo)}); return data;")

    dataInfoIen = len(dataInfo)
    bodyInfoArray = []
    bodyAttributeArray = []
    for i in range(dataInfoIen):
        if i%2 == 0:
            bodyAttributeArray.append(dataInfo[i]['arr'])
            bodyInfoArray.append(dataInfo[i]['bodyInfo'].replace(' ','').replace('\n',''))


    # tableHtml = html_soup.find_element_by_id('listPlayer')
    # table_rows = tableHtml.find_elements_by_tag_name('tr')
    # newsList = html_soup.find('table',{'class':'tb-team table table-hover table-striped'}).tbody.tr.td[4]
    newsList = html_soup.find_all('table')

    trList = []
    for tr in newsList[0].tbody.find_all('tr'):
        tdList = []
        for td in tr.find_all('td'):
            showText = td.get_text().replace(' ','').replace('\n','')
            tdList.append(showText)
        del tdList[0]
        del tdList[0]
        del tdList[0]
        trList.append(tdList)
    # print(trList)
    # pdb.set_trace() # 运行到这里会自动暂停

    attributeList = html_soup.find_all('div',{'class':'box-poses-list'})
    attributeListArray = []

    for i in attributeList:
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

    # print(attributeListArray)
    # pdb.set_trace() # 运行到这里会自动暂停

    nameClassList = html_soup.find_all('span',{'class':'item-player'})
    nameArraySet = []
    imgArraySet = []
    nameClassListSet = []

    for i in nameClassList:
        nameClassListSet.append(i)

    nameClassListSetLen = len(nameClassListSet)
    for i in range(nameClassListSetLen):
        if i%2 == 0:
            imgArraySet.append('https://www.ol4vs.com/'+nameClassListSet[i].a.img.get('src'))
        else:
            nameArraySet.append(nameClassListSet[i].a.get_text())

    # print(imgArraySet)
    # print(nameArraySet)
    # pdb.set_trace() # 运行到这里会自动暂停

    itemArrayset = []
    itemLen = len(trList)
    for i in range(itemLen):
        itemSet = {}
        itemSet['country'] = trList[i][0] #国籍
        itemSet['ability_value'] = trList[i][1] #能力值
        itemSet['salary'] = trList[i][2] #薪水
        itemSet['name'] = nameArraySet[i] #名字
        itemSet['salary'] = imgArraySet[i] #头像
        itemSet['attribute'] = attributeListArray[i] #属性
        itemSet['bodyAttributeArray'] = bodyAttributeArray[i] #详情属性
        itemSet['bodyInfoArray'] = bodyInfoArray[i] #详情，身高，体重等等
        print(itemSet)
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

