# -*- coding: utf-8 -*-
def trapping_rain(buildings):
    total_height = 0 # 총 갇히는 비의 양을 담을 변수
    n = len(buildings)

    # 각각 왼쪽 오른쪽 최대값 리스트 정의
    left_list = [0] * n
    right_list = [0] * n

    # buildings 리스트 각 인덱스 별로 왼쪽으로의 최댓값을 저장한다
    left_list[0] = buildings[0]
    for i in range(1, n):
        left_list[i] = max(left_list[i - 1], buildings[i])

    # buildings 리스트 각 인덱스 별로 오른쪽으로의 최댓값을 저장한다
    right_list[-1] = buildings[-1]
    for i in range(n - 2, -1, -1):
        right_list[i] = max(right_list[i + 1], buildings[i])

    # 저장한 값들을 이용해서 총 갇히는 비의 양을 계산한다
    for i in range(n):
        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(right_list[i], left_list[i])

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])

    return total_height

print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


# 시간 복잡도
# 인풋 buildings의 길이를 n이라고 부릅시다.
#
# 각 for 문의 반복 횟수는 n에 비례합니다. n에 비례하는 for 문이 세 개여도 결국 다 n에 비례하기 때문에 trapping_rain 함수의 시간 복잡도는 O(n)입니다.
#
# 공간 복잡도
# n에 비례하는 길이의 리스트 2개를 사용하기 때문에 공간 복잡도는 O(n)이 됩니다.
