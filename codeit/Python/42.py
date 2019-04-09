# -*- coding: utf-8 -*-
# 이진 탐색 - 반복문
# 선형 탐색 알고리즘과 달리, 정렬된 리스트를 전제로 합니다.
# 왜 이 알고리즘의 이름이 '이진 탐색'일까요? 1회 비교를 거칠 때마다 탐색 범위가 절반으로 줄어들기 때문입니다.

def binary_search(element, some_list):
    # 코드를 작성하세요.
    left = 0
    right = len(some_list) - 1

    while left <= right:
        center = (left + right) // 2
        if element < some_list[center]:
            right = center - 1
        elif element > some_list[center]:
            left = center + 1
        elif element == some_list[center]:
            return center

    return "None"

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
