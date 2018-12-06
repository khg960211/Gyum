# -*- coding: utf-8 -*-

import os
import hashlib
import sys
import zlib
import StringIO
import scanmod # scanmod 모듈을 import
import curemod
import imp # 외부 모듈을 동적으로 import 하기 위한 모듈

VirusDB = [] # 악성코드 패턴은 모두 virus.db에 존재함
vdb = [] # 가공된 악성코드 DB가 저장된다.
vsize = [] # 악성코드 파일 크기만 저장한다.
sdb = [] # 가공된 악성코드 DB가 저장된다.(특정위치검색법용)

# KMD 파일을 복호화한다.
def DecodeKMD(fname) :
    try :
        fp = open(fname, 'rb')
        buf = fp.read()
        fp.close()

        buf2 = buf[:-32] # 암호화 내용을 분리한다.
        fmd5 = buf[-32:] # MD5를 분리한다.

        f = buf2
        for i in range(3) : # 암호화 내용의 MD5를 구한다.
            md5 = hashlib.md5()
            md5.update(f)
            f = md5.hexdigest()

        if f != fmd5 : # 위 결과와 파일에서 분리된 MD5가 같은가?
            raise SystemError

        buf3 = ''
        for c in buf2[4:] : # 0xFF로 XOR 한다.
            buf3 += chr(ord(c) ^ 0xFF)

        buf4 = zlib.decompress(buf3) # 압축을 해제한다.
        return buf4 # 성공했다면 복호화된 내용을 리턴한다.
    except :
        pass

    return None # 오류가 있다면 None을 리턴한다.

# virus.kmd 파일에서 악성코드 패턴을 읽는다.
def LoadVirusDB() :
    buf = DecodeKMD('virus.kmd') # 악성코드 패턴을 복호화한다.
    fp = open('virus.db', 'rb')

    while True :
        line = fp.readline() # 악성코드 패턴을 한 줄 읽는다.
        if not line : break # 읽어들인 line이 파일의 끝이거나 문제가 발생했다면 작업을 중단한다.

        line = line.strip() # line의 뒤쪽에는 엔터키('\r\n')ㅇ; 추가되어 있기 때문에 이를 제거한다.
        VirusDB.append(line) # 악성코드 패턴을 VirusDB에 추가한다.

    fp.close()

# VirusDB를 가공하여 vdb에 저장한다.
def MakeVirusDB() :
    for pattern in VirusDB :
        t = []
        v = pattern.split(':') # 세미콜론을 기준으로 자른다.

        scan_func = v[0] # 악성코드 검사 함수
        cure_func = v[1] # 악성코드 치료 함수

        if scan_func == 'ScanMD5' : # MD5 해시를 이용한 검사인가?
            t.append(v[3]) # MD5 해시를 저장한다.
            t.append(v[4]) # 악성코드 이름을 저장한다.
            vdb.append(t) # 최종 vdb에 저장한다.

            size = int(v[2]) # 악성코드 파일 크기
            if vsize.count(size) == 0 : # 이미 해당 크기가 등록되었나?
                vsize.append(size)
        elif scan_func == 'ScanStr' : # 특정 위치 검색법인가?
            t.append(int(v[2])) # 악성코드 진단 문자열의 위치를 저장한다.
            t.append(v[3]) # 악성코드 진단 문자열을 저장한다.
            t.append(v[4]) # 악성코드 이름을 저장한다.
            sdb.append(t) # 최종 sdb에 저장한다.

if __name__ == '__main__' :
    LoadVirusDB() # 악성코드 패턴을 파일에서 읽는다.
    MakeVirusDB() # 악성코드 DB를 가공한다.

    # 커맨드라인으로 악성코드를 검사할 수 있게 한다.
    # 커맨드라인의 입력 방식을 체크한다.
    if len(sys.argv) != 2 :
        print 'Usage : antivirus.py [file]'
        os.system('pause')
        sys.exit(0)

    fname = sys.argv[1] # 악성코드 검사 대상 파일

    try : # 외부 scanmod 모듈을 로딩하여 그 내부의 ScanVirus 함수를 실행하여 악성코드를 검사한다.
        m = 'scanmod' # 동적 로딩할 모듈의 이름(파일이름)
        f, filename, desc = imp.find_module(m, ['']) # 현재 폴더에서 모듈을 찾음
        module = imp.load_module(m, f, filename, desc) # 찾은 모듈을 로딩함
        # 진단 함수 호출 명령어 구성 작업
        cmd = 'ret, vname = module.ScanVirus(vdb, vsize, sdb, fname)'
        exec cmd # 명령어 실행
    except ImportError : # 만약 외부에 존재하는 scanmod 모듈을 동적 import에 실패하면 except 영역의 내부 scanmod 모듈의 ScanVirus 함수를 실행한다.
        ret, vname = scanmod.ScanVirus(vdb, vsize, sdb, fname)

    if ret == True :
        print '%s : %s' % (fname, vname)
        curemod.CureDelete(fname) # 파일을 삭제해서 치료
    else :
        print '%s : ok' % (fname)
else :
    print '%s : ok' % (fname)
