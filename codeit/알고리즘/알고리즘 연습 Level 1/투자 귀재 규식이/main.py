# -*- coding: utf-8 -*-
# 내가 짠 코드

def sublist_max(profits):
    # 코드를 작성하세요.
    a = []
    sum_i = 0
    for i in profits:
        sum_i = sum_i + i
        a.append(sum_i)
    index_i = max(a)
    return index_i
#   return profits[:a.index(index_i)+1] 하면 수익이 높은 구간이 나옴


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))
