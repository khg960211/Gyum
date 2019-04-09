# -*- coding: utf-8 -*-
# 내가 짠 코드
# 리스트에 담겨있는 튜플들은 각각 하나의 수업을 나타냅니다.
# 각 튜플의 0번째 항목은 해당 수업의 시작 시간, 그리고 1 번 항목은 해당 수업이 끝나는 시간입니다.
# 예를 들어서 0번 인덱스에 있는 튜플값은 (4, 7)이니까, 해당 수업은 4교시에 시작해서 7교시에 끝나는 거죠.
# (2, 5)를 듣는다고 가정합시다. (4, 7) 수업은 (2, 5)가 끝나기 전에 시작하기 때문에, 두 수업은 같이 들을 수 없습니다.
# 반면, 수업 (1, 3)과 (4, 7)은 시간이 겹치지 않기 때문에 동시에 들을 수 있습니다.
# 열정이 불타오르는 신입생 지웅이는 최대한 많은 수업을 들을 수 있는 수업 조합을 찾아주는 함수 course_selection 함수를 작성하려고 합니다.
# course_selection은 파라미터로 전체 수업 리스트를 받고 가능한 많은 수업을 담은 리스트를 리턴합니다.


def course_selection(course_list):
    # 코드를 작성하세요.
    sorted_list = sorted(course_list, key=lambda x: x[1])

    i = 0
    while i < len(sorted_list) - 1:
        if sorted_list[i][1] > sorted_list[i+1][0]:
            del sorted_list[i+1]
            i -= 1
            if i < 0:
                i = 0
            continue

        i += 1

    return sorted_list

# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
