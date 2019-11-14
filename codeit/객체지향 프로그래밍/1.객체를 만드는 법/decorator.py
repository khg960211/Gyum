# -*- coding: utf-8 -*-
# 데코레이터 함수

def add_print_to(original):
    def wrapper():
        print("함수 시작") #부가기능
        original()
        print("함수 끝") #부가기능
    return wrapper

@add_print_to # print_hello를 add_print_to로 꾸며주어라
def print_hello():
    print("안녕하세요!")


# print_hello = add_print_to(print_hello) # add_print_to(print_hello)()
print_hello()
