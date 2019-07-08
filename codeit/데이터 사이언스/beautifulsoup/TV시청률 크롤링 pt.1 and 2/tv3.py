import requests

# 코드를 작성하세요
url = "https://workey.codeit.kr/ratings/index/"
r = requests.get(url)
rating_page = r.text
#page = requests.get("https://workey.codeit.kr/ratings/index")
#rating_page = BeautifulSoup(page.text, 'html.parser')
# 출력 코드
print(rating_page)
