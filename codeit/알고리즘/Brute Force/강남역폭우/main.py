# -*- coding: utf-8 -*-
# 내가 짠 코드
def trapping_rain(buildings):
    # 코드를 작성하세요
    result = 0

    for i in range(len(buildings)):
        left_tall = 0
        right_tall = 0

        if i == 0:
            left_tall = buildings[i]
        for j in buildings[:i]:
            if left_tall == 0:
                left_tall = j
            elif left_tall < j:
                left_tall = j
                break
        for k in buildings[i:]:
            if right_tall == 0:
                right_tall = k
            elif right_tall < k:
                right_tall = k
                break
        if left_tall > right_tall:
            result = result + (right_tall - buildings[i])
        else:
            if (left_tall - buildings[i]) > 0:
            	result = result + (left_tall - buildings[i])

    return result


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
