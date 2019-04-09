# -*- coding: utf-8 -*-
# 28.py와 동일
# __init__()을 통해 인스턴스 생성과 초기값 설정을 한번에 해결할 수 있다.
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

user1 = User("Young", "young@codeit.kr", "123456")
print(user1.email)
