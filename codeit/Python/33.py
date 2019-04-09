# -*- coding: utf-8 -*-
# 피보나치 수열

# n번째 피보나치 수를 리턴
def fib(n):
    # 코드를 입력하세요.
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# 테스트: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))
