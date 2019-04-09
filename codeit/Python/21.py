# -*- coding: utf-8 -*-
# 매출 파일 열기
in_file = open('chicken.txt', 'r', encoding='utf-8')
amount = 0
count = 0

# 파일 각 줄 읽기
for line in in_file:
    data = line.strip().split(": ")
    amount += int(data[1])
    count += 1

print(amount / count)

# 파일 닫기
in_file.close()
