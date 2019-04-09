# -*- coding: utf-8 -*-
# 해답
def fib(n):
    # base case
    if n < 3:
        return 1

    # recursive case
    return fib(n - 1) + fib(n - 2)

# 테스트: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))
