# -*- coding: utf-8 -*-
# 내가 짠 코드
# n 번째 피보나치 수를 계산하기 위해서는 가장 최근에 계산한 두 값만 알면 된다.

def fib_optimized(n):
    # 코드를 작성하세요.
    current = 1
    previous = 0

    if n == 1:
        return current

    for i in range(n-1):
        temp = current
        current = current + previous
        previous = temp
    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
