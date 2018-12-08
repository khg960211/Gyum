# -*- coding: utf-8 -*-
import hashlib
import os
import py_compile
import random
import shutil
import struct
import sys
import zlib
import k2rc4
import k2rsa
import k2timelib

#-------------------------------------------------------------------------------
# make(src_fname)
# rsa 개인키를 이용해서 주어진 파일을 암호화하여 KMD 파일을 생성한다.
# 입력값 : src_fname - 암호화 대상 파일
# 리턴값 : kmd 파일 생성 성공 여부
#-------------------------------------------------------------------------------
def make(src_fname, debug=False):
    #---------------------------------------------------------------------------
    # 암호화 대상 파일을 컴파일 또는 복사해서 준비한다.
    #---------------------------------------------------------------------------
    fname = src_fname

    if fname.split('.')[1] == 'py': # 파이썬 파일을 컴파일한다.
        py_compile.compile(fname)   # 컴파일
        pyc_name = fname+'c'        # 컴파일 이후 파일명
    else: # 파이썬 파일이 아닐 경우 확장자를 pyc로 하여 복사한다.
        pyc_name = fname.split('.')[0]+'.pyc'
        shutil.copy(fname, pyc_name)

    #---------------------------------------------------------------------------
    # Simple RSA를 사용하기 위해 공개키와 개인키를 로딩한다.
    #---------------------------------------------------------------------------

    # 공개키를 로딩한다.
    rsa_pu = k2rsa.read_key('key.pkr')
    # print 'pkr : ', rsa_pu

    # 개인키를 로딩한다.
    rsa_pr = k2rsa.read_key('key_skr')
    # print 'skr : ', rsa_pr

    if not (rsa_pr and rsa_pu): # 키 파일을 찾을 수 없다.
        if debug:
            print 'ERROR : Cannot find the key files!'
        return False

    #---------------------------------------------------------------------------
    # KMD 파일을 생성한다.
    #---------------------------------------------------------------------------
    # 헤더 : 시그니처(KAVM) + 예약 영역 : [[KAVM][날짜][시간]...]
    #---------------------------------------------------------------------------
    # 시그니처(KAVM)을 추가한다.
    kmd_data = 'KAVM'

    # 현재 날짜와 시간을 구한다.
    ret_date = k2timelib.get_now_date()
    ret_time = k2timelib.get_now_time()

    # 날짜와 시간 값을 2Byte로 변경한다.
    val_date = struct.pack('<H', ret_date)
    val_time = struct.pack('<H', ret_time)

    reserved_buf = val_date + val_time + (chr(0) * 28) # 예약 영역

    # 날짜/시간 값이 포함된 예약 영역을 만들어 추가한다.
    kmd_data += reserved_buf

    #---------------------------------------------------------------------------
    # 본문 : [[개인키로 암호화한 RC4 키][RC4로 암호화한 파일]]
    #---------------------------------------------------------------------------
    random.seed()

    while 1:
        tmp_kmd_data = '' # 임시 본문 데이터

        # RC4 알고리즘에 사용할 128bit 랜덤키 생성
        key = ''
        for i in range(16):
            key += chr(random.randint(0, 0xff))

        # 생성된 RC4 키를 암호화한다.
        e_key = k2rsa.crypt(key, rsa_pr) # 개인키로 암호화
        if len(e_key) != 32: # 암호화에 오류가 존재하면 다시 생성
            continue

        # 암호화된 RC4 키를 복호화한다.
        d_key = k2rsa.crypt(e_key, rsa_pu) # 공개키로 복호화

        # 생성된 RC4 키에 문제없음을 확인한다.
        if key == d_key and len(key) == len(d_key):
            # 개인키로 암호화된 RC4 키를 임시 버퍼에 추가한다.
            tmp_kmd_data += e_key

            # 생성된 pyc 파일 압축하기
            buf1 = open(pyc_name, 'rb').read()
            buf2 = zlib.compress(buf1)

            e_rc4 = k2rc4.RC4() # RC4 알고리즘 사용
            e_rc4.set_key(key) # RC4 알고리즘에 key를 적용한다.

            # 압축된 pyc 파일 이미지를 RC4로 암호화한다.
            buf3 = e_rc4.crypt(buf2)

            e_rc4 = k2rc4.RC4() # RC4 알고리즘 사용
            e_rc4.set_key(key) # RC4 알고리즘에 key를 적용한다.

            # 암호화한 압축된 pyc 이미지 파일 이미지 복호화하여 결과가 같은지 확인한다.
            if e_rc4.crypt(buf3) != buf2:
                continue

            # 개인키로 암호화한 압축된 파일 이미지를 임시 버퍼에 추가한다.
            tmp_kmd_data += buf3

            #-------------------------------------------------------------------
            # 꼬리 : [개인키로 암호화한 MD5 X 3]
            #-------------------------------------------------------------------
            # 헤더와 본문에 대해 MD5를 3번 연속 구한다.
            md5 = hashlib.md5()
            md5hash = kmd_data + tmp_kmd_data # 헤더와 본문을 합쳐서 MD5 계산

            for i in range(3):
                md5.update(md5hash)
                md5hash = md5.hexdigest()

            m = md5hash.decode('hex')

            e_md5 = k2rsa.crypt(m, rsa_pr) # MD5 결과를 개인키로 암호화
            if len(e_md5) != 32: # 암호화에 오류가 존재하면 다시 생성
                continue

            d_md5 = k2rsa.crypt(e_md5, rsa_pu) # 암호화된 MD5를 공개키로 복호화

            if m == d_md5:  # 원문과 복호화 결과가 같은가?
                # 헤더, 본문, 꼬리를 모두 합친다.
                kmd_data += tmp_kmd_data + e_md5
                break # 무한 루프를 종료한다.

#-------------------------------------------------------------------------------
# KMD 파일을 생성한다.
#-------------------------------------------------------------------------------
# KMD 파일 이름을 만든다.
ext = fname.fine('.')
kmd_name = fname[0:ext] + '.kmd'

try:
    if kmd_data:
        # KMD파일을 생성한다.
        open(kmd_name, 'wb').write(kmd_data)

        # pyc 파일은 삭제한다.
        os.remove(pyc_name)

        if degub:
            print ' Success : %-13s -> %s' % (fname, kmd_name)
        return True
    else:
        raise IOError
except IOError:
    if debug:
        print ' Fail : %s' % fname
    return False
