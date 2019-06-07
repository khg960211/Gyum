# -*- coding: utf-8 -*-
# 브루트포스 방식
# stock_list의 길이를 n이라고 하면 시간 복잡도는 O(n^2)
def max_profit(stock_list):
    # 현재까지의 최대 수익
    max_profit_so_far = stock_list[1] - stock_list[0]

    # 한 번 사고 파는 모든 조합을 본다.
    for i in range(len(stock_list) - 1):
        for j in range(i+1, len(stock_list)):
            # i에서 사고 j에 파는 것이 현재까지의 최대 수익이라면 max_so_far를 바꾼다.
            max_profit_so_far = max(max_profit_so_far, stock_list[j] - stock_list[i])

    return max_profit_so_far

# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))
