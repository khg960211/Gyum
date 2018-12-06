# -*- coding: utf-8 -*-

import os
import hashlib

fp = open('eicar_test.txt', 'rb') # 바이너리 모드로 읽기
fbuf = fp.read()
fp.close()

m = hashlib.md5()
m.update(fbuf)
fmd5 = m.hexdigest()

# EICAR Test 파일 MD5 와 비교
if fmd5 == '44d88612fea8a8f36de82e1278abb02f' :
    print 'Virus'
    os.remove('eicar_test.txt') # 파일을 삭제해서 치료
else :
    print 'No Virus'
