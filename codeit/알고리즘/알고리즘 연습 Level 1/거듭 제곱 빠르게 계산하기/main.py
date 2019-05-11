# -*- coding: utf-8 -*-
# 내가 짠 코드

def power(x, y):
    # 코드를 작성하세요.
    if y < 2:
        return x * y

    result = power(x, y // 2)

    if y % 2 == 0:
        return result * result
    else:
        return result * result * x

# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))
