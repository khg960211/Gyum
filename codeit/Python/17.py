# -*- coding: utf-8 -*-
# 자리수 합 리턴
def sum_digit(num):
    str_num = str(num)
    sum = 0
    
    # 각 자리수를 sum_digit에 추가
    for digit in str_num:
        sum = sum + int(digit)
    return sum

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 코드를 입력하세요.
result = 0
for i in range(1, 1001):
    result += sum_digit(i)
print(result)
