# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

years = list(range(2010, 2019))
months = list(range(1, 13))
weeks = list(range(0, 5))

nielsen_pages = []

for year in years:
    for month in months:
        for week in weeks:
            response = requests.get("https://workey.codeit.kr/nielsen/index?year=" + str(year) + "&month=" + str(month) + "&weekIndex=" + str(week))
            nielsen_pages.append(BeautifulSoup(response.content, 'html.parser'))

# 테스트 코드
print(len(nielsen_pages)) # 가져온 총 페이지 수
print(nielsen_pages[0]) # 첫 번째 페이지의 HTML 코드
