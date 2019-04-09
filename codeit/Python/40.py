# -*- coding: utf-8 -*-
# 합병 정렬

# 두 리스트 합치기
def merge(list1, list2):
    # 코드를 입력하세요.
    i = 0
    j = 0
    merge_list = []

    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merge_list.append(list2[j])
            j += 1
        elif list1[i] < list2[j]:
            merge_list.append(list1[i])
            i += 1

    if i == len(list1):
        while j < len(list2):
            merge_list.append(list2[j])
            j += 1
    elif j == len(list2):
        while i < len(list1):
            merge_list.append(list1[i])
            i += 1

    return merge_list

# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.
    if len(my_list) <= 1:
        return my_list

    left = my_list[:len(my_list) // 2]
    right = my_list[len(my_list) // 2:]

    return merge(merge_sort(left), merge_sort(right))

some_list = [11, 3, 6, 4, 12, 1, 2]
sorted_list = merge_sort(some_list)
print(sorted_list)
