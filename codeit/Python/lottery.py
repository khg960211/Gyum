# -*- coding: utf-8 -*-
# 로또 시뮬레이션 프로그램

from random import randint

# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    numbers = []

    # 6개 뽑을 때까지 반복
    while len(numbers) < 6:
        rand_num = randint(1, 45)

        # 새로운 수 나올 때까지 다시 뽑기
        while rand_num in numbers:
            rand_num = randint(1, 45)
        numbers.append(rand_num)

    numbers = sorted(numbers) # 6개의 당첨 번호 정렬

    return numbers

# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    win_numbers = generate_numbers()
    # 보너스 번호 뽑기
    bonus_num = randint(1, 45)
    while bonus_num in win_numbers:
        bonus_num = randint(1, 45)
    win_numbers.append(bonus_num)

    return win_numbers

# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    count = 0
    i = 0
    while i < len(list1):
        if list1[i] in list2:
            count += 1
        i += 1

    return count
    # for i in range(len(list1)):
    #     for j in range(len(list2)):
    #         if list1[i] == list2[j]:
    #             count += 1
    #
    # return count

# 로또 등수 확인하기
def check(numbers, winning_numbers):
    # match = count_matching_numbers(numbers, winning_numbers)
    match = count_matching_numbers(numbers, winning_numbers[:6])
    if match == 6:
        return int(1000000000)
    elif match == 5 and winning_numbers[6] in numbers:
        return int(50000000)
    elif match == 5:
        return int(1000000)
    elif match == 4:
        return int(50000)
    elif match == 3:
        return int(5000)
    else:
        return int(0)
