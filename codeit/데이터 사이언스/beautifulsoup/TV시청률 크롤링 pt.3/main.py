# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# 기간 지정
years = list(range(2010, 2019))
months = list(range(1, 13))
weeks = list(range(0, 5))

# 빈 리스트 생성
rating_pages = []

for year in years:
    for month in months:
        for week in weeks:
            # HTML 코드 받아오기
            response = requests.get("https://workey.codeit.kr/ratings/index?year=" + str(year) + "&month=" + str(month) + "&weekIndex=" + str(week))

            # BeautifulSoup 타입으로 변환하기
            soup = BeautifulSoup(response.text, 'html.parser')

            # "row" 클래스가 1개를 넘는 경우만 페이지를 리스트에 추가
            if len(soup.select('.row')) > 1:
                rating_pages.append(response.text)

# 테스트 코드
print(len(rating_pages)) # 가져온 총 페이지 수
print(rating_pages[0]) # 첫 번째 페이지의 HTML 코드
