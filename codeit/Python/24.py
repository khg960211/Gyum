# -*- coding: utf-8 -*-

in_file = open('vocabulary.txt', 'r')

for line in in_file:
    data = line.strip().split(": ")
    answer = input("%s: " % (data[0]))
    mean = data[1]
    if answer == mean:
        print("맞았습니다!")
    else:
        print("아쉽습니다. 정답은 %s입니다." % (mean))

in_file.close()
