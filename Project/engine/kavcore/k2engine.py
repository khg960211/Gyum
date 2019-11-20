# -*- coding: utf-8 -*-

import os
import StringIO

import k2kmdfile
import k2rsa

#-------------------------------------------------------------------------------
# Engine 클래스
#-------------------------------------------------------------------------------
class Engine:
    #---------------------------------------------------------------------------
    # __init__(self, debug=False)
    # 클래스를 초기화한다.
    # 인자값 : debug - 디버그 여부
    #---------------------------------------------------------------------------
    def __init__(self, debug=False):
        self.debug = debug # 디버깅 여부

        self.plugins_path = None # 플러그인 경로
        self.kmdfiles = [] # 우선순위가 기록된 kmd 리스트

    #---------------------------------------------------------------------------
    # set_plugins(self, plugins_path)
    # 주어진 경로에서 플러그인 엔진을 로딩 준비한다.
    # 인자값 : plugins_path - 플러그인 엔진 경로
    # 리턴값 : 성공 여부
    #---------------------------------------------------------------------------
    def set_plugins(self, plugins_path):
        # 플러그인 경로를 저장한다.
        self.plugins_path = plugins_path

        # 공개키를 로딩한다.
        pu = k2rsa.read_key(plugins_path + os.sep + 'key.pkr')
        if not pu:
            return False

        # 우선순위를 알아낸다.
        ret = self.__get_kmd_list(plugins_path + os.sep + 'kicom.kmd', pu)
        if not ret: # 로딩할 KMD 파일이 없다.
            return False

        if self.debug:
            print '[*] kicom.kmd : '
            print '     ', self.kmdfiles

        return True

    #---------------------------------------------------------------------------
    # __get_kmd_list(self, kicom_kmd_file, pu)
    # 플러그인 엔진의 로딩 우선순위를 알아낸다.
    # 인자값 : kmcom_kmd_file - kicom.kmd 파일의 전체 경로
    #          pu            - 공개키
    # 리턴값 : 성공 여부
    #---------------------------------------------------------------------------
    def __get_kmd_list(self, kicom_kmd_file, pu):
        kmdfiles = [] # 우선순위 목록

        k = k2kmdfile.KMD(kicom_kmd_file, pu) # kicom.kmd 파일을 복호화한다.

        if k.body:  # kicom.kmd 파일이 읽혔는가?
            msg = StringIO.StringIO(k.body)

            while True:
                # 한 줄을 읽어 엔터키 제거
                line = msg.readline().strip()

                if not line: # 읽혀진 내용이 없으면 종료
                    break
                elif line.find('.kmd') != -1: # KMD 확장자가 존재한다면
                    kmdfiles.append(line) # KMD 우선순위 목록에 추가
                else: # 확장자가 KMD가 아니면 다음 파일로...
                    continue

        if len(kmdfiles):   # 우선순위 목록에 하나라도 있으면 성공
            self.kmdfiles = kmdfiles
            return True
        else: # 우선순위 목록에 아무것도 없으면 실패
            return False
