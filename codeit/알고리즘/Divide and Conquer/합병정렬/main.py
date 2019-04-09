# -*- coding: utf-8 -*-
# 합병 정렬 구현하기
# 내가 짠 코드
def merge(list1, list2):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
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
        elif list1[0] == list2[0]:
            merged_list.append(list1[0])
            del list1[0]

    return merged_list

# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.
    if len(my_list) < 2:
        return my_list
    left_half = my_list[0:len(my_list)//2]
    right_half = my_list[len(my_list)//2:]

    return merge(merge_sort(left_half), merge_sort(right_half))
# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
