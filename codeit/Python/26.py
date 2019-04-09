# -*- coding: utf-8 -*-
# 사전을 활용한 고급 단어장

from random import randint

dic = {}

in_file = open('vocabulary.txt', 'r')

for line in in_file:
    data = line.strip().split(": ")
    dic[data[0]] = data[1]

keys = list(dic.keys()) # 영어단어 리스트

while True:
    index = randint(0, len(keys) - 1)
    eng = keys[index]
    answer = input("%s: " % (dic[eng]))
    if answer == eng:
        print("맞았습니다!\n")
    elif answer == 'q':
        break
    else:
        print("틀렸습니다. 정답은 %s입니다.\n" % (eng))

in_file.close()
