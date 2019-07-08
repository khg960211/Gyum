# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# 코드를 작성하세요
response = requests.get("https://workey.codeit.kr/music/index")
soup = BeautifulSoup(response.text, 'html.parser')

name_tags = soup.select(".rank .list")
search_ranks = []

for name in name_tags:
    temp = name.text.strip().split(' ')
    search_ranks.append(temp[2])
# 결과 출력
print(search_ranks)
