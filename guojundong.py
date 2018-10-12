from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("D:\pythonFile\chromedriver_win32\chromedriver.exe")
driver.get('https://www.ol4vs.com')
html = driver.page_source    # 获取网页html
html_soup = BeautifulSoup(html,"html.parser")
# tableHtml = html_soup.find_element_by_id('listPlayer')
# table_rows = tableHtml.find_elements_by_tag_name('tr')
# newsList = html_soup.find('table',{'class':'tb-team table table-hover table-striped'}).tbody.tr.td[4]
newsList = html_soup.find_all('table')

for tr in newsList[0].tbody.find_all('tr'):
    for td in tr.find_all('td'):
        showText = td.get_text().replace(' ','').replace('\n','')
        print(showText) 

# for row in range(1,10):
#     # table_col = table_rows[row].find_elements_by_tag_name('td')
#     # for col in range(1,6):
#     #     showText = table_rows[row].find_elements_by_tag_name('td')[col].text.replace(' ','').replace('\n','')
#     #     print(showText)
#     showNengLiZhi = table_rows[row].find_elements_by_tag_name('td')[4].text