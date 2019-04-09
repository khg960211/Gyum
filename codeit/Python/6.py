# -*- coding: utf-8 -*- 
# 거스름돈 계산기
def calculate_change(payment, cost):
    change = payment - cost

    fifty_thousand = int(change / 50000)
    change = change % 50000

    ten_thousand = int(change / 10000)
    change = change % 10000

    five_thousand = int(change / 5000)
    change = change % 5000

    thousand = int(change / 1000)

    print("50000원 지폐 : %d장" % fifty_thousand)
    print("10000원 지폐 : %d장" % ten_thousand)
    print("5000원 지폐 : %d장" % five_thousand)
    print("1000원 지폐 : %d장" % thousand)


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
