# -*- coding: utf-8 -*-
# 해설

def fib_optimized(n):
    current = 1
    previous = 0

    # 반복적으로 위 변수들을 업데이트한다.
    for i in range(1, n):
        current, previous = current + previous, current # 이렇게 하면 임시 저장 변수 없이, 한 줄에 작성 가능

    # n번재 피보나치 수를 리턴한다.
    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
