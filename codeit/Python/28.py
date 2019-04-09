# -*- coding: utf-8 -*-
class User:
    # initialize 메소드를 여기 쓰세요
    # def initialize...
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")

user2 = User()
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User()
user3.initialize("Taeho", "taeho@codeit.kr", "123abc")

user4 = User()
user4.initialize("Lisa", "lisa@codeit.kr", "abc123")

print(user1.email)
print(user2.name)
print(user3.password)
print(user4.email)
