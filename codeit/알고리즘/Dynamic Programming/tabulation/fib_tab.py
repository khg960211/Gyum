# -*- coding: utf-8 -*-
# tabulation 활용한 피보나치 수 구하기
# 내가 짠 코드

def fib_tab(n):
    # code
    fib_table = [1, 1]
    sum = 0
    for i in range(1, n + 1):
        if i < 3:
            sum = sum + fib_table[i - 1]
            continue
        fib_table.append(sum)
        sum = sum + fib_table[i - 2]

    return fib_table[n - 1]


# test
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))
