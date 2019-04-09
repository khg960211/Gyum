# -*- coding: utf-8 -*-
# 선형 탐색
# 리스트의 처음부터 끝까지 순서대로 하나씩 탐색을 진행하는 알고리즘

def linear_search(element, some_list):
    # 코드를 작성하세요.
    for i in range(len(some_list)):
        if element == some_list[i]:
            return i

    return None

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))
