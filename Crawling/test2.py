# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Twitter
from sklearn.linear_model import LogisticRegression # 이진 분류 알고리즘
from sklearn.model_selection import GridSearchCV # 하이퍼파라미터 최적화

url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=156083&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'

def get_reple(page = 1):
    response = requests.get(url.format(page))
    soup = BeautifulSoup(response.text, 'html.parser')

    s, t = [], []

    for li in soup.find('div', {'class': 'score_result'}).find_all('li'):
        # print("점수:", li.em.text)
        # print("댓글:", li.p.text)
        if int(li.em.text) >= 8:
            s.append(1)
            t.append(li.p.text)
        elif int(li.em.text) <= 5:
            s.append(0)
            t.append(li.p.text)
        return s, t

twitter = Twitter()
score, text = [], []
for i in range(1, 1000):
    time.sleep(1)
    print('요청 횟수:', i, end='\r')
    s, t = get_reple(i)
    score += s
    text += t

df = pd.DataFrame([score, text]).T
df.to_csv('test.csv')

train_x, test_x, train_y, test_y = train_test_split(text, score, test_size=0.2, random_state=0)
tfv = TfidfVectorizer(min_df=3, max_df=0.9)
tfv.fit(train_x)
tfv_train_x = tfv.transform(train_x)

clf = LogisticRegression(random_state=0)
params = {'C': [1, 3, 5, 7, 9]}
grid_cv = GridSearchCV(clf, param_grid=params, cv=4, scoring='accuracy', verbose=1)
grid_cv.fit(tfv_train_x, train_y)

tfv_test_x = tfv.transform(test_x)
grid_cv.best_estimator_.score(tfv_test_x, test_y)
