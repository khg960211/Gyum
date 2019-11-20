# -*- coding: utf-8 -*-
import k2rsa
import k2kmdfile

# 개인키와 공개키를 생성한다.
k2rsa.create_key('key.pkr', 'key.skr')

# 특정 파일(readme.txt)를 kmd 파일로 만든다.
ret = k2kmdfile.make('readme.txt')
if ret: # 성공
    pu = k2rsa.read_key('key.pkr') # 복호화할 공개키를 로딩한다.
    k = k2kmdfile.KMD('readme.kmd', pu) # readme.kmd 파일 읽기
    print(k.body) # readme.txt 파일 내용이 출력된다.
    print("Success")
