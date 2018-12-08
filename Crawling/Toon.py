# -*- coding: utf-8 -*-
# 웹툰 추출 프로그램
from __future__ import unicode_literals
import os
import requests
from bs4 import BeautifulSoup
import sys
import re
from PyQt5.QtWidgets import *

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

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Webtoon")
        self.setGeometry(500, 500, 500, 200)
        self.setupUI()

    def setupUI(self):
        # Label
        label = QLabel("URL", self)
        label.move(20, 20)

        # LineEdit
        self.lineEdit = QLineEdit("", self)
        self.lineEdit.resize(400, 30)
        url = self.lineEdit.text()
        self.lineEdit.move(80, 20)

        # button
        btn1 = QPushButton("추출", self)
        btn1.move(80, 100)
        btn1.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        url = self.lineEdit.text()
        crawl_naver_webtoon(url)
        QMessageBox.about(self, "message", "완료!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
