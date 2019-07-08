# -*- coding: utf-8 -*-
def sum_in_list(search_sum, sorted_list):
    low = 0
    high = len(sorted_list) - 1
    while low < high:
        if sorted_list[low] + sorted_list[high] == search_sum:
            return True
        elif sorted_list[low] + sorted_list[high] < search_sum:
            low += 1
        else:
            high -= 1

    return False



print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))
