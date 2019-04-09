# -*- coding: utf-8 -*-
# 해답
def triangle_number(n):
    # base case
    if n == 1:
        return 1

    # recursive case
    return n + triangle_number(n - 1)

for i in range(1, 11):
    print(triangle_number(i))
