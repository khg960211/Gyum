# -*- coding: utf-8 -*-

def merge(list1, list2):
    # 코드를 입력하세요.
    merged_list = []

    if len(list1) == 0:
        merged_list.append(list2[0])
        del list2[0]
    elif len(list2) == 0:
        merged_list.append(list1[0])
        del list1[0]

    while len(list1) != 0 or len(list2) != 0:
        if len(list1) == 0:
            merged_list.append(list2[0])
            del list2[0]
        elif len(list2) == 0:
            merged_list.append(list1[0])
            del list1[0]

        elif list1[0] < list2[0]:
            merged_list.append(list1[0])
            del list1[0]
        elif list1[0] > list2[0]:
            merged_list.append(list2[0])
            del list2[0]



    return merged_list

# 테스트
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))
