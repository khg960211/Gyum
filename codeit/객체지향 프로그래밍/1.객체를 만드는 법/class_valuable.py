# -*- coding: utf-8 -*-
class User:
    count = 0 #클래스 변수, 한 클래스의 모든 인스턴스가 공유하는 속성

    def __init__(self, name, email, pw):
        # 유저 인스턴스의 모든 변수를 지정해주는 메소드
        self.name = name
        self.email = email
        self.pw = pw
        User.count += 1

#User.count = 1
#print(User.count)

user1 = User("강영훈", "younghoon@codeit.kr", "123456")
user2 = User("김현겸", "1234@5678.kr", "67890")

user1.count = 5

print(User.count)
print(user1.count)
print(user2.count)
