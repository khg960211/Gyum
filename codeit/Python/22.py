# -*- coding: utf-8 -*-
# 파일 쓰기

# 파일 열기
out_file = open('new_file.txt', 'w')

# 파일에 쓰기
out_file.write("Hello World!\n")
out_file.write("My name is HyunGyum Kim!")

# 파일 닫기
out_file.close()
