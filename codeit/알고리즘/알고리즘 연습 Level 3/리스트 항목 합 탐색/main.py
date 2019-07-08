# -*- coding: utf-8 -*-
# Brute Force 방법
# 인풋 리스트의 길이가 n이라고 할 때 시간 복잡도는 O(n^2)
def sum_in_list(search_sum, sorted_list):
    # 코드를 쓰세요
    for i in range(len(sorted_list)-1):
        for j in range(i, len(sorted_list)-1):
            if (search_sum == sorted_list[i] + sorted_list[j]):
                return True
    return False


print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))
