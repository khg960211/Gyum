# -*- coding: utf-8 -*-
# 이진 탐색 - 재귀 함수

def binary_search(element, some_list, start_index = 0, end_index = None):
    if end_index == None:
        end_index = len(some_list) - 1

    # 코드를 작성하세요.
    if start_index > end_index:
        return None

    center = (start_index + end_index) // 2

    if element == some_list[center]:
        return center
    elif element > some_list[center]:
        start_index = center + 1
        return binary_search(element, some_list, start_index, end_index)
    else:
        end_index = center - 1
        return binary_search(element, some_list, start_index, end_index)


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
