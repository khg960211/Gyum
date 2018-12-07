# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from urllib.request import urlopen
from bs4 import BeautifulSoup


class qlabel(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.text = QTextBrowser(self)
        html  = urlopen("https://music.bugs.co.kr/chart/track/week/total")
        soup = BeautifulSoup(html.read(), "html.parser")
        cnt_artist = 0
        cnt_title = 0
        self.text.resize(600, 600)
        self.text.append("벅스뮤직 top 100 순위 입니다.")
        for link1 in soup.find_all("p", {"class":"artist"}):
            cnt_artist += 1
            self.text.append(str(cnt_artist) + "위")
            self.text.append("아티스트 : "+link1.find('a').text)

        self.text.append("------------------------------")

        for link2 in soup.find_all("p", {"class":"title"}):
            cnt_title += 1
            self.text.append(str(cnt_title) + "위")
            self.text.append("노래제목 : "+link2.find('a').text)

        self.setGeometry(500, 500, 700, 600)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ql = qlabel()
    sys.exit(app.exec())
