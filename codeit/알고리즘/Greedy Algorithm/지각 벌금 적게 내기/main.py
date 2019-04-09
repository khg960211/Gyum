# -*- coding: utf-8 -*-
# 내가 짠 코드
# 익중이네 밴드부는 매주 수요일 오후 6시에 합주를 하는데요. 멤버들이 너무 상습적으로 늦어서, 1분에 1달러씩 내야 하는 벌금 제도를 도입했습니다.
# 그런데 마침 익중이와 친구 넷이 놀다가 또 지각할 위기입니다. 아직 악보도 출력해 놓지 않은 상황이죠.
# 어차피 같이 놀다 늦은 것이니 벌금을 다섯 명이서 똑같이 나눠 내기로 하고, 벌금을 가능한 적게 내는 방법을 고민해 보기로 합니다.
# 다섯 사람이 각각 출력해야 하는 페이지 수는 3장, 1장, 4장, 3장, 2장입니다. 프린터는 한 대밖에 없고, 1장을 출력하기 위해서는 1분이 걸립니다.
def min_fee(pages_to_print):
    # 코드를 작성하세요.
    result = 0

    while(len(pages_to_print) > 0):
        result = result + min(pages_to_print) * len(pages_to_print)
        del pages_to_print[pages_to_print.index(min(pages_to_print))]

    return result


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
