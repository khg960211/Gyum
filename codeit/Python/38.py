# -*- coding: utf-8 -*-
# 선택 정렬

def selection_sort(my_list):
    # 코드를 입력하세요.
    for i in range(len(my_list) - 1):
        least_num = my_list[i]

        # 2번째 값부터 least_num과 비교하여 제일 작은 값을 least_num에 저장
        for j in range(i + 1, len(my_list)):
            if least_num > my_list[j]:
                least_num = my_list[j]
                index_num = j

        # 첫 번째 값부터 least_num과 비교하여 값이 least_num보다 크면 두 숫자를 바꾼다.
        if my_list[i] > least_num:
            temp = my_list[i]
            my_list[i] = least_num
            my_list[index_num] = temp

    return my_list

    # 모범 답안
    # def selection_sort(my_list):
    # # 바깥쪽 반복문
    # for i in range(len(my_list)):
    #     min_index = i
    #
    #     # 안쪽 반복문
    #     for j in range(i + 1, len(my_list)):
    #         value = my_list[j]
    #         if value < my_list[min_index]:
    #             min_index = j
    #
    #     # 자리 바꾸기
    #     temp = my_list[i]
    #     my_list[i] = my_list[min_index]
    #     my_list[min_index] = temp

some_list = [11, 3, 6, 4, 12, 1, 2]
selection_sort(some_list)
print(some_list)
