def binary_search(element, some_list):
    left = 0
    right = len(some_list) - 1

    while left <= right:
        center = (left + right) // 2
        if element == some_list[center]:
            return center
        elif element < some_list[center]:
            right = center - 1
        else:
            left = center + 1
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
