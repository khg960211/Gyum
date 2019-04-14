# -*- coding: utf-8 -*-
# 내가 짠 코드

def select_stops(water_stops, capacity):
    # 코드를 작성하세요.
    water = []
    original_cap = capacity
    idx = 0
    for i in water_stops:
        if i < capacity:
            idx += 1
            continue
        else:
            if water_stops[idx] > capacity:
                water.append(water_stops[idx-1])
                capacity = water_stops[idx-1] + original_cap
                idx += 1
                continue
            water.append(water_stops[idx])
            capacity = water_stops[idx] + original_cap
            idx += 1

    water.append(water_stops[len(water_stops)-1])
    return water


# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))
