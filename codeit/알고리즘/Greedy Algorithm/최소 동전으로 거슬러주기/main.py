# -*- coding: utf-8 -*-
# 내가 짠 코드
# 최소 동전으로 돈을 거슬러주는 함수

def min_coin_count(value, coin_list):
    # 코드를 작성하세요.
    sum = 0
    remain = value % coin_list[1]
    sum = sum + (value // coin_list[1])
    sum = sum + (remain // coin_list[0])
    remain = value % coin_list[0]
    sum = sum + (remain // coin_list[3])
    remain = value % coin_list[3]
    sum = sum + (remain // coin_list[2])
    remain = value % coin_list[2]

    return sum

# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))
