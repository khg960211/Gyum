# -*- coding: utf-8 -*-
# 운명적인 그녀를 만났습니다. 하지만 오렌지 보틀에서 일한다는 것 말고는 아는 게 전혀 없네요.
# 오렌지 보틀의 웹사이트에 가서, 모든 지점의 전화번호를 모아보려고 합니다.
# 모든 지점의 전화번호가 포함된 리스트를 print 해 보세요.
import requests
from bs4 import BeautifulSoup

# 코드를 작성하세요
response = requests.get("https://workey.codeit.kr/orangebottle/index")
soup = BeautifulSoup(response.text, 'html.parser')

span_tags = soup.select(".branch span")

phone_numbers = []

for span in span_tags:
    phone_numbers.append(span.text.strip())
# 결과 출력
print(phone_numbers)
