# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import requests
from bs4 import BeautifulSoup
import sys
import re


def crawl_naver_webtoon(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    comic_title = ' '.join(soup.select('.comicinfo h2')[0].text.split())
    comic_title = comic_title.replace(' ', '')
    comic_title = re.sub('[-=.#/?:$]', '', comic_title)
    ep_title = ' '.join(soup.select('.tit_area h3')[0].text.split())

    for img_tag in soup.select('.wt_viewer img'):
        image_file_url = img_tag['src']
        image_dir_path = os.path.join(os.path.dirname(__file__), comic_title, ep_title)
        image_file_path = os.path.join(image_dir_path, os.path.basename(image_file_url))

        if not os.path.exists(image_dir_path):
            os.makedirs(image_dir_path)

        print(image_file_path)

        headers = {'Referer': url}
        image_file_data = requests.get(image_file_url, headers=headers).content
        open(image_file_path, 'wb').write(image_file_data)

    print('Completed !')

if __name__ == '__main__':
    if len(sys.argv) is 1:
        print('Usage [webtoon.py "url"]')
    else:
        url = sys.argv[1]
        # episode_url = 'http://comic.naver.com/webtoon/detail.nhn?titleId=20853&no=1048&weekday=tue'
        crawl_naver_webtoon(url)
