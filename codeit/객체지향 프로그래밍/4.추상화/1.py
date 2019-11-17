# -*- coding: utf-8 -*-
class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000

    def __init__(self, name, password, payment_limit):
        # 코드를 쓰세요
        self.__name = name
        self.__password = password
        self.__payment_limit = payment_limit

    # 코드를 쓰세요
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_password(self):
        return "비밀 번호는 볼 수 없습니다"

    def set_password(self, new_password):
        self.__password = new_password

    def get_payment_limit(self):
        return self.__payment_limit

    def set_payment_limit(self, new_payment_limit):
        if 0 < new_payment_limit  and new_payment_limit < MAX_PAYMENT_LIMIT:
            self.__payment_limit = new_payment_limit
        else:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해주세요!")

card = CreditCard("강영훈", "123", 100000)

print(card.get_name())
print(card.get_password())
print(card.get_payment_limit())

card.set_name("성태호")
card.set_password("1234")
card.set_payment_limit(-10)

print(card.get_name())
print(card.get_password())
print(card.get_payment_limit())
