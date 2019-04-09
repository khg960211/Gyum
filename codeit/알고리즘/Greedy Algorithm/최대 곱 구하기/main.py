# -*- coding: utf-8 -*-
# 내가 짠 코드
# 각 플레이어는 3장의 카드를 들고 있다. 한 사람당 카드 하나씩 뽑았을 때 모두 곱해서 가능한 최대 곱을 출력하게 하라
def max_product(card_lists):
    # 코드를 작성하세요.
    result = 1

    for i in range(len(card_lists)):
        big = 0
        for j in range(len(card_lists[i])):
            if big == 0:
                big = card_lists[i][0]
            elif big < card_lists[i][j]:
                big = card_lists[i][j]
        result *= big

    return result


# 테스트
test_cards1 = [[1, 6, 5], [4, 2, 3]]
print(max_product(test_cards1))

test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
print(max_product(test_cards2))

test_cards3 = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
print(max_product(test_cards3))

test_cards4 = [[5, 5, 5], [4, 3, 5], [1, 1, 1], [9, 8, 3], [2, 8, 4], [5, 7, 4]]
print(max_product(test_cards4))
