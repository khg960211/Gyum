# -*- coding: utf-8 -*-
# 파이썬에서 queue 사용하기

from collections import deque

# 새로운 queue 생성
numbers = deque()

# queue에 값 추가
numbers.append(2)
numbers.append(3)
numbers.append(5)
numbers.append(7)

print(numbers)
print(len(numbers))

# queue에서 하나 제거
x = numbers.popleft()
print(x)
print(numbers)
print(len(numbers))

# queue에서 하나 제거
x = numbers.popleft()
print(x)
print(numbers)
print(len(numbers))
