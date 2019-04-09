# -*- coding: utf-8 -*-
# chicken.txt 파일을 읽어서 한 줄씩 출력
in_file = open('chicken.txt', 'r')

for line in in_file:
    print(line)

in_file.close()
