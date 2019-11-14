# -*- coding: utf-8 -*-
class User:
    count = 0 #클래스 변수, 한 클래스의 모든 인스턴스가 공유하는 속성

    def __init__(self, name, email, pw):
        # 유저 인스턴스의 모든 변수를 지정해주는 메소드
        self.name = name
        self.email = email
        self.pw = pw
        User.count += 1

    def say_hello(self):
        # 인사 메세지 출력 메소드
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def __str__(self): # 던더 메소드(dunder method), print함수를 호출할 때 자동으로 불려짐
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

    # @classmethod #데코레이터
    # def number_of_users(cls): #클래스 메소드의 첫번째 규. 첫 번째 파라미터의 이름은 꼭 cls로 쓰기
    #     print("총 유저 수는: {}입니다.".format(cls.count))

    def number_of_users(self):
        print("총 유저 수는: {}입니다.".format(User.count))

user1 = User("강영훈", "younghoon@codeit.kr", "123455")
user2 = User("이윤수", "yoonsoo@codeit.kr", "123456")
user3 = User("서혜린", "lisa@codeit.kr", "123abc")


User.number_of_users(user1)
user1.number_of_users()

# 인스턴스 메소드는 인스턴스 자신이 첫 번째 파라미터로 자동 전달됨
# 클래스 메소드는 첫 번째 파라미터로 클래스가 자동 전달됨

# 인스턴스 변수를 사용하면 인스턴스 메소드를 사용
# 클래스 변수를 사용하면 클래스 메소드를 사용

# 클래스 변수와 인스턴스 변수 둘 다 쓴다면?
# 인스턴스 메소드를 쓰면 인스턴스 변수, 클래스 변수 모두 사용 가능
# 클래스 메소드는 인스턴스 변수 사용 불가
