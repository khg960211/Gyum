# -*- coding: utf-8 -*-
# 정수 n을 입력받으면 n의 각 자릿 수의 합을 출력

# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    # 코드를 작성하세요.
    if len(str(n)) == 1:
        return n
    sum = n // 10 ** (len(str(n)) - 1)
    n = n % 10 ** (len(str(n)) - 1)
    return sum_digits(n) + sum

# # n의 각 자릿수의 합을 리턴
# def sum_digits(n):
#     if n < 10:
#         return n
#     else:
#         str_n = str(n)
#         return int(str_n[0]) + sum_digits(int(str_n[1:]))

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))
