# -*- coding: utf-8 -*-
# 내가 짠 코드
# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store1[1]) ** 2 + (store2[0] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    # 여기 코드를 쓰세요
    small_distance = 0
    for store1 in test_coordinates:
        for store2 in test_coordinates:
            if store1 != store2:
                if small_distance == 0:
	                small_distance = distance(store1, store2)
                elif small_distance > distance(store1, store2):
                    small_distance = distance(store1, store2)
                    storeA = store1
                    storeB = store2
    return storeA, storeB

# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))
