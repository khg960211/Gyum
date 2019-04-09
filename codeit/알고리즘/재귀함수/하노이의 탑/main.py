# -*- coding: utf-8 -*-
# 내가 짠 코드
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_discs, start_peg, end_peg):
    # 코드를 입력하세요.
    # base case : 옮길 원판이 없으면 함수를 끝낸다.
    if num_discs == 0:
        return
    elif num_discs == 1:
        return move_disk(num_discs, start_peg, end_peg)
    # n-1개를 2번 기둥으로 옮긴다.
    # n번째 원판을 3번 기둥으로 옮긴다.
    # n-1개의 원판을 3번 기둥으로 옮긴다.
    hanoi(num_discs-1, start_peg, 6-start_peg-end_peg)
    move_disk(num_discs, start_peg, end_peg)
    hanoi(num_discs-1, 6-start_peg-end_peg, end_peg)

# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3)
