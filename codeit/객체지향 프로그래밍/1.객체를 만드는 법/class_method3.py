# -*- coding: utf-8 -*-
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_param):
        # 코드를 쓰세요

        # cls.params_list = string_params.split(",")
        # name = cls.params_list[0]
        # email = cls.params_list[1]
        # password = cls.params_list[2]
        # return cls(name, email, password)
        
        string_param = string_param.split(",")
        return cls(string_param[0], string_param[1], string_param[2])

    @classmethod
    def from_list(cls, list_param):
        # 코드를 쓰세요
        return cls(list_param[0], list_param[1], list_param[2])

# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)
