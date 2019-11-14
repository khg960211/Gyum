# -*- coding: utf-8 -*-
class User:
    # initialize 메소드를 여기 쓰세요
    # def initialize...
    def __init__(self, name, email, password): #인스턴스가 생성될 때 자동으로 호출됨
        self.name = name
        self.email = email
        self.password = password

user1 = User("Young", "young@codeit.kr", "123456")
# user1.initialize("Young", "young@codeit.kr", "123456")

user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User("Taeho", "taeho@codeit.kr", "123abc")

user4 = User("Lisa", "lisa@codeit.kr", "abc123")



print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)
