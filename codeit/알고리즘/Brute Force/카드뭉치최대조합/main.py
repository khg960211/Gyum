# -*- coding: utf-8 -*-
# 내가 짠 코드
def max_product(left_cards, right_cards):
    # 코드를 작성하세요.
    biggest = 0

    for i in left_cards:
        for j in right_cards:
            if biggest == 0:
                biggest = i * j
            if biggest < i * j:
                biggest = i * j

    return biggest


# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))
