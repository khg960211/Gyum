# -*- coding: utf-8 -*-
# 내가 짠 코드
# memoization의 max_profit이랑 같은 문제
# price_list는 개수별 가격이 정리되어 있는 리스트
# count는 판매할 새콤달콤 개수

# 답은 맞았지만, 확인 결과 코드 잘못 짬..다시 공부할 것

def max_profit(price_list, count):
    # 코드를 작성하세요.
    profit_tab = [0]

    for i in range(1, count+1):
        if i < 2:
            profit_tab.append(price_list[i])
        else:
            price =[]
            if i >= len(price_list):
                price_list.append(0)
            for j in range(1, i // 2 + 1):
                if i % j == 0:
                    price.append(price_list[i / j] * j)
                price.append(max(price_list[i], price_list[i - j] + price_list[i - (i - j)]))
            profit_tab.append(max(price))


    return profit_tab[count]


# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
