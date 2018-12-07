# -*- coding: utf-8 -*-
import k2rc4

# Test 코드
if __name__ == '__main__':
    rc4 = k2rc4.RC4()
    rc4.set_key('PASSWORD1234') # 암호 설정
    t1 = rc4.crypt('hello') # 암호화

    rc4 = k2rc4.RC4()
    rc4.set_key('PASSWORD1234') # 암호 설정
    t2 = rc4.crypt(t1) # 복호화
    print t2 # 결과 확인
