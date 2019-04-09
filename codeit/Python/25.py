# -*- coding: utf-8 -*-

# 사전(dictionary)
# key - value

dict1 = {}

dict1[5] = 25
dict1[2] = 4
dict1[3] = 9
print(dict1)
print(dict1[3])

family = {}
family['mom'] = 'grace'
family['dad'] = 'chris'
family['son'] = 'young'
family['daughter'] = 'kay'
print(family)
print(family['dad'])
print(family.keys()) # key들만 전부 가져오기 위해서 keys 메소드 사용
print('son' in family.keys()) # 어떤 키가 있는지 확인
print('uncle' in family.keys())
print(family.values()) # value들을 모두 받아오기 위해 values 메소드 사용
print('grace' in family.values()) # 어떤 value가 있는지 확인

# family의 key들을 리스트로 쓰고 싶다면 list 함수를 쓴다.
family_keys = list(family.keys())
print(family_keys)
# value도 똑같다.
family_values = list(family.values())
print(family_values)
