from urllib.request import urlopen, Request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from tqdm import tqdm
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys
import warnings
warnings.filterwarnings(action='ignore')

SCROLL_DOWN_TIME = 1.5 # 스크롤 내리는 시간
#===============================================================================================
# Chrome Driver로 url 생성
baseUrl = "https://www.instagram.com/explore/tags/"
plusUrl = input('태그입력 : ')
url = baseUrl + quote_plus(plusUrl)

print('Chrome Driver 실행중...')
driver = webdriver.Chrome('C:\webdriver\chromedriver.exe')
driver.get(url)
time.sleep(3)

#==================================================================================================
# 자동로그인... 인스타그램 로그인 단계가 늘어남으로 오류가 생겨서 보류
#login_section = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button'
#driver.find_element_by_xpath(login_section).click()
#time.sleep(2)

#elem_login = driver.find_element_by_name("username")
#elem_login.clear()
#elem_login.send_keys('ID') #내 인스타 아이디

#elem_login = driver.find_element_by_name('password')
#elem_login.clear()
#elem_login.send_keys('PASSWORD') #내 인스타 비밀번호
#time.sleep(2)

#xpath = """//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button"""
#driver.find_element_by_xpath(xpath).click()
#time.sleep(4)

#==================================================================================================
# 총 게시물 숫자 불러오기
pageString = driver.page_source
bsObj = BeautifulSoup(pageString, 'lxml')
temp_data = bsObj.find_all(name='meta')[-1]
temp_data = str(temp_data)
start = temp_data.find('게시물') + 4
end = temp_data.find('개')
total_post_data = temp_data[start:end]
print("총 {0}개의 게시물이 검색되었습니다.".format(total_post_data))
print('태그를 수집하는 중입니다...')

#==================================================================================================
reallink = [] # 전체 게시물 링크 저장

# url 화면에서 스크롤을 내리면서 게시물 크롤링
while True:
    pageString = driver.page_source
    bsObj = BeautifulSoup(pageString, 'lxml')

    for link1 in bsObj.find_all(name='div', attrs={"class":"Nnq7C weEfm"}):
        title = link1.select('a')[0]
        real = title.attrs['href']
        reallink.append(real)
        title = link1.select('a')[1]
        real = title.attrs['href']
        reallink.append(real)
        title = link1.select('a')[2]
        real = title.attrs['href']
        reallink.append(real)

    last_scroll = driver.execute_script('return document.body.scrollHeight')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_DOWN_TIME)
    new_scroll = driver.execute_script("return document.body.scrollHeight")

    if new_scroll == last_scroll:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_DOWN_TIME)
        new_scroll = driver.execute_script("return document.body.scrollHeight")

        # 현재 게시물이 마지막 게시물일 때 break
        if new_scroll == last_scroll:
            break
        else:
            last_scroll = new_scroll
            continue

    time.sleep(2)

total_tag_data = len(reallink) # 전체 태그 데이터의 크기 저장

print('{0}개의 태그를 수집합니다.'.format(total_tag_data))
csvtext = []

#==================================================================================================
# 프로그램 실시간 진행률을 알기 위한 tqdm 라이브러리 사용
for i in tqdm(range(total_tag_data)):
    csvtext.append([])
    req = Request("https://www.instagram.com/p"+reallink[i], headers={'User-Agent': 'Mozila/5.0'})

    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'lxml', from_encoding='utf-8')
    soup1 = soup.find('meta', attrs={'property':"og:description"})

    reallink1 = soup1['content']
    reallink1 = reallink1[reallink1.find("@") + 1:reallink1.find(")")]
    reallink1 = reallink1[:20]

    if reallink1 == '':
        reallink1 = "Null"
    csvtext[i].append(reallink1)

    for reallink2 in soup.find_all('meta', attrs={'property':"instapp:hashtags"}):
        hashtags = reallink2['content'].rstrip(',')
        csvtext[i].append(hashtags)

    time.sleep(0.5)

    # 데이터를 csv파일, txt파일로 저장
    data = pd.DataFrame(csvtext)
    data.to_csv('tagdata.csv', encoding='utf-8-sig')
    data.to_csv('tagdata.txt', encoding='utf-8')

#==================================================================================================

driver.close() # Chrome Driver 종료
