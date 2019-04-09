# -*- coding: utf-8 -*-
# 리스트 연습
numbers = []
numbers.append(5)
print(numbers)
numbers.append(8)
print(numbers)
print(len(numbers))


numbers2 = [1, 2, 3, 4, 5, 6, 7, 8]
del numbers2[3]
print(numbers2)
numbers2.insert(5, 0) # numbers2의 인덱스 5 자리에 0을 넣어라
print(numbers2)

print(sorted(numbers2)) # 내용물 오름차순으로 정렬

numbers3 = numbers + numbers2
print(numbers3)
