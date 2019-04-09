# -*- coding: utf-8 -*-
# 해답
def max_product(card_lists):
    # 누적된 곱을 저장하는 변수
    product = 1

    # 반복문을 돌면서 카드 뭉치를 하나씩 본다
    for card_list in card_lists:
        # product에 각 뭉치의 최댓값을 곱해 준다
        product *= max(card_list)

    return product


# 테스트
test_cards1 = [[1, 6, 5], [4, 2, 3]]
print(max_product(test_cards1))

test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
print(max_product(test_cards2))
