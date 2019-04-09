# -*- coding: utf-8 -*-
# 내가 짠 코드
# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp
    index1 += 1
    index2 += 1
    return index1, index2


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 코드를 작성하세요.
    p = end
    b = 0
    for i in range(len(my_list)-1):
        if my_list[p] > my_list[i]:
            b, i = swap_elements(my_list, b, i)

        elif my_list[p] < my_list[i]:
            pass
    b, i = swap_elements(my_list, b, p)
    return my_list.index(my_list[b-1])

# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)
