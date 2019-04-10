# -*- coding: utf-8 -*-
# 내가 짠 코드
# 새콤달콤 장사로 벌어들일 수 있는 최대 수익을 구하라.
# price_list : 개수 별 가격이 정리되어 있는 리스트
# count : 판매할 새콤달콤 개수
# cache : 개수별 최대 수익이 저장되어 있는 사전
# price_list가 [0, 100, 400, 800, 900, 1000] 이라면 0개에 0원, 1개에 100원, 2개에 400원, 3개에 800원, 4개에 900원, 5개에 1000원의 가격
# 만약 5개를 판다면 한 사람에게 3개, 다른 사람에게 2개를 팔아서 1200원의 수익을 내는 것이 최대 수익이다.

def max_profit_memo(price_list, count, cache):
    # 코드를 작성하세요.
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]
    if count in cache:
        return cache[count]

    result = []
    if len(price_list) <= count:
        result.append(0)
    else:
        result.append(price_list[count])
    for i in range(1, count):
        result.append(max_profit_memo(price_list, count - i, cache) + max_profit_memo(price_list, count - (count - i), cache))
    cache[count] = max(result)

    return cache[count]



def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
