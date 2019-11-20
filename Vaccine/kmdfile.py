# -*- coding: utf-8 -*-

import k2rsa
import k2kmdfile

pu = k2rsa.read_key('key.pkr') # 복호화할 공개키를 로딩한다.
k = k2kmdfile.KMD('dummy.kmd', pu) # dummy.kmd 파일 읽기

# k.body에 dummy.kmd의 파이썬 코드가 복호화된다.
module = k2kmdfile.load('dummy', k.body) # dummy 플러그인 엔진 모듈을 등록한다.

#-------------------------------------------------------------------------------
# 사용 방법 (1)
# kmdfile.load 함수의 리턴값으로 직접 사용 가능
#-------------------------------------------------------------------------------
kav = module.KavMain() # dummy 플러그인 엔진의 KavMain 인스턴스를 생성한다.
kav.init('.') # 플러그인 엔진을 초기화한다.
print kav.getinfo()
kav.uninit()

#-------------------------------------------------------------------------------
# 사용 방법 (2)
# import dummy로도 사용 가능
#-------------------------------------------------------------------------------
import dummy

kav2 = dummy.KavMain()
kav2.init('.') # 플러그인 엔진을 초기화 한다.
print kav2.listvirus() # 진단/치료 가능한 악성코드 리스트를 얻는다.
kav2.uninit() # 플러그인 엔진을 종료한다.
