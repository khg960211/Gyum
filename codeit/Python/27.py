# -*- coding: utf-8 -*-
# 클래스, User 자료형 만들기

class User:
    def say_my_name(self): # 클래스 내에 정의된 함수 = 메소드
        print("My name is " + self.name)
    def introduce(self, n):
        for i in range(n):
            print("%s is %d years old" % (self.name, self.age))

user1 = User() # 인스터스(user1) 생성
user3 = user1
print(type(user1))

user2 = User()
print(user1 == user2)
print(user1 == user3)

user1.name = "Young" # 인스턴스 변수 설정(name, email...등등)
user1.email = "young@codeit.kr"
user1. password = "123456"
user1.age = 18
user2.name = "Yoonsoo"
user2. email = "yoonsoo@codeit.kr"
user2.password = "abcdef"

User.say_my_name(user1)
user1.say_my_name()
User.introduce(user1, 3)
user1.introduce(3)
