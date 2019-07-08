# -*- coding: utf-8 -*-
def find_same_number(some_list, start = 1, end = None):
    if end == None:
        end = len(some_list) - 1

    # 반복 요소를 찾으면 리턴한다
    if start == end:
        return start

    # 중간 지점을 구한다
    mid = (start + end) // 2

    # 왼쪽 범위의 숫자를 센다. 오른쪽은 리스트 길이에서 왼쪽 길이를 빼면 되기 때문에 세지 않는다
    left_count = 0

    for element in some_list:
        if start <= element and element <= mid:
            left_count += 1

    # 왼쪽과 오른쪽 범위중 과반 수 이상의 숫자가 있는 범위 내에서 탐색을 다시한다
    if left_count > mid - start + 1:
        return find_same_number(some_list, start, mid)
    return find_same_number(some_list, mid + 1, end)

print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))

# 시간 복잡도
# 인풋 리스트의 길이를 n이라고 했을 때, 탐색 범위를 줄일 때마다 리스트의 모든 요소 n개를 돌면서 두 개의 범위 안에 있는 자연수의 갯수를 세고 있습니다. 한 번 리스트를 돌 때마다 시간 복잡도는 O(n)입니다.
#
# 범위의 크기는 (n−1)/2에서 시작해서 계속 반으로 줄어듭니다. 최악의 경우 범위가 자연수 하나가 되는 데까지 O(lg(n))가 걸리죠.
#
# 범위가 줄어들 때마다 O(n)의 작업을 하고, 범위는 최악의 경우 총 O(lg(n))번 줄어들기 때문에 최종 시간 복잡도는 O(nlg(n))이 됩니다.
