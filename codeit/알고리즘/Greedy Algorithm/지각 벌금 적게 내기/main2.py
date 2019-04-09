# -*- coding: utf-8 -*-
# 해답

def minimum_total_fee(pages_to_print):
    # 인풋으로 받은 리스트를 정렬시켜 준다
    sorted_list = sorted(pages_to_print)

    # 총 벌금을 담을 변수
    total_fee = 0

    # 정렬된 리스트에서 총 벌금 계산
    for i in range(len(sorted_list)):
        total_fee += sorted_list[i] * (len(sorted_list) - i)

    return total_fee


# 테스트
print(minimum_total_fee([3, 1, 4, 3, 2]))

# 인풋 리스트 pages_to_print의 길이를 n이라고 하자.
# 리스트를 정렬시켜 주는 부분이 O(n lg n)이고
# for문 부분이 O(n)이다.
# 합하면 O(n lg n + n)이기 때문에 결국 시간복잡도는 O(nlgn)이다.
