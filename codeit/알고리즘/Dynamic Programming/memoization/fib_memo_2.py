# -*- coding: utf-8 -*-
# memoization 활용한 피보나치 수 계산
# 해설

# n번째 피보나치 수를 담는 사전
fib_cache = {}

def fib_memo(n):
    # base case
    if n < 3:
        return 1

    # 이미 n번째 피보나치를 계산했으면:
    # 저장된 값을 바로 리턴한다
    if n in fib_cache:
        return fib_cache[n]

    # 아직 n번째 피보나치 수를 계산하지 않았으면:
    # 계산을 한 후 cache에 저장
    fib_cache[n] = fib_memo(n - 1) + fib_memo(n - 2)

    # 계산한 값을 리턴한다
    return fib_cache[n]

# 테스트
print(fib_memo(10))
print(fib_memo(50))
print(fib_memo(100))
