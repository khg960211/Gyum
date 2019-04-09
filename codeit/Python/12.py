# -*- coding: utf-8 -*-
# 리스트 연습
# 빈 리스트 만들기
numbers = []

# 1부터 10까지의 값을 리스트에 차례대로 넣어주기
i = 0
while i < 10:
    numbers.append(i + 1)
    i += 1
print(numbers)

# 리스트 값 중에 홀수인 값들 제거
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        del numbers[i]
    else: # 이렇게 해주지 않으면 numbers[0] 값이 삭제되었을 때 numbers[1]값이 자동으로 numbers[0]이 되어버려 2로 나누어지는지 아닌지 확인을 못하기 때문
        i += 1
print(numbers)

numbers.insert(0, 20)
print(numbers)

print(sorted(numbers))
