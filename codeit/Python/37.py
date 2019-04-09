# -*- coding: utf-8 -*-
# 하노이의 탑
# 하노이의 탑 게임의 해답을 출력해주는 함수 hanoi를 쓰세요.
# hanoi는 파라미터로 원판 수 num_discs, 게임을 시작하는 기둥 번호 start_peg, 그리고 목표로 하는 기둥 번호 end_peg를 받고,
# 재귀적으로 문제를 풀어 원판을 옮기는 순서를 모두 출력합니다.

def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_discs, start_peg = 1, end_peg = 3):
    if num_discs == 0:
        return
    else:
        other_peg = 6 - start_peg - end_peg
        # 1번 기둥 2번 기둥 3번 기둥 숫자의 합은 6이다.
        hanoi(num_discs - 1, start_peg, other_peg)
        move_disk(num_discs, start_peg, end_peg)
        hanoi(num_discs - 1, other_peg, end_peg)

hanoi(3, 1, 3)
# hanoi(1, 2, 3)
