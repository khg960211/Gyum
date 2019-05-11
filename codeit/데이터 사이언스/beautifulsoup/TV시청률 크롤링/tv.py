import requests
from bs4 import BeautifulSoup

# 코드를 작성하세요
nielsen_pages = []
year = 2010
month = 1
weekIndex = 0
while year < 2019:
    while month < 13:
        while weekIndex < 5:
            page = requests.get("https://workey.codeit.kr/nielsen/index?year="+ str(year) +"&month=" + str(month) + "&weekIndex=" + str(weekIndex))
            nielsen_pages.append(BeautifulSoup(page.text, 'html.parser'))
            weekIndex += 1
        weekIndex = 0
        month += 1
    month = 1
    year += 1

# 테스트 코드
print(len(nielsen_pages)) # 가져온 총 페이지 수
print(nielsen_pages[0]) # 첫 번째 페이지의 HTML 코드
