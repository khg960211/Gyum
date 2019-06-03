# -*- coding: utf-8 -*-
def find_same_number(some_list):
    # 이미 나온 요소를 저장시켜줄 사전
    elements_seen_so_far = {}

    for element in some_list:
        # 이미 나온 요소인지 확인하고 맞으면 요소를 리턴한다
        if element in elements_seen_so_far:
            return element

        # 해당 요소를 사전에 저장시킨다
        elements_seen_so_far[element] = True

print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
