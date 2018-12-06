# -*- coding: utf-8 -*-

fp = open('eicar_test.txt', 'rb') # 바이너리 모드로 읽기
fbuf = fp.read()
fp.close()

if fbuf[0:3] == 'X50' : # 파일 맨 앞 3Byte가 'X50'인가?
    print 'Virus'
    os.remove('eicar_test.txt') # 파일을 삭제해서 치료
else :
    print 'No Virus'
