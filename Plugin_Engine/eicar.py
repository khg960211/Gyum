# -*- coding: utf-8 -*-
# Author : Kei Choi (hanul93@gmail.com)

import os
import hashlib

class KavMain:
    # ----------------------------------------------------------------------------
    # init(self, plugins_path)
    # 플러그인 엔진을 초기화한다.
    # 인자값 : plugins_path - 플러그인 엔진의 위치
    # 리턴값 : 0 - 성공, 0 이외의 값 - 실패
    # ----------------------------------------------------------------------------
    def init(self, plugins_path): # 플러그인 엔진 초기화한다
        # 진단/치료하는 악성코드 이름
        return 0 # 플러그인 엔진 초기화 성공

    # ----------------------------------------------------------------------------
    # uninit(self)
    # 플러그인 엔진을 종료한다.
    # 리턴값 : 0 - 성공, 0 이외의 값 - 실패
    # ----------------------------------------------------------------------------
    def uninit(self): # 플러그인 엔진 종료

        return 0

    # ----------------------------------------------------------------------------
    # scan(self, filehandle, filename)
    # 악성코드를 검사한다.
    # 인자값 : filehandle  - 파일 핸들
    #       : filename    - 파일 이름
    # 리턴값 : ( 악성코드 발견 여부, 악성코드 이름, 악성코드 ID ) 등등
    # ----------------------------------------------------------------------------
    def scan(self, filehandle, filename):
        try:
            mm = filehandle

            size = os.path.getsize(filename) # 검사 대상 파일 크기를 구한다.
            if size == 68: # EICAR Test 악성코드의 크기와 일치하는가?
                # 크기가 일치한다면 MD5 해시 계산
                m = hashlib.md5()
                m.update(mm[:68])
                fmd5 = m.hexdigest()
                # 파일에서 얻은 해시값과 EICAR Test 악성코드의 해시 값이 일치하는가?
                if fmd5 == '44d88612fea8a8f36de82e1278abb02f':
                    return True, 'EICAR-Test-File (not a virus)', 0
        except IOError:
            pass

        # 악성코드를 발견하지 못했음을 리턴한다.
        return False, '', -1

    # ----------------------------------------------------------------------------
    # disinfect(self, filename, malware_id)
    # 악성코드를 치료한다.
    # 인자값 : filename    - 파일 이름
    #       : malware_id  - 치료할 악성코드 ID
    # 리턴값 : 악성코드 치료 여부
    # ----------------------------------------------------------------------------
    def disinfect(self, filename, malware_id): # 악성코드 치료
        try:
            # 악성코드 진단 결과에서 받은 ID 값이 0인가?
            if malware_id == 0:
                os.remove(filename) # 파일 삭제
                return True # 치료 완료 리턴

        except IOError:
            pass

        return False # 치료 실패 리턴

    # ----------------------------------------------------------------------------
    # listvirus(self)
    # 진단/치료 가능한 악성코드의 목록을 알려준다.
    # 리턴값 : 악성코드 치료 여부
    # ----------------------------------------------------------------------------
    def listvirus(self): # 진단 가능한 악성코드 목록
        vlist = list() # 리스트형 변수 선언

        vlist.append('EICAR-Test-File (not a virus)') # 진단/치료하는 악성코드 이름 등록

        return vlist # 진단/치료 가능한 악성코드의 이름을 모두 vlist에 등록했다면 리턴한다.

    # ----------------------------------------------------------------------------
    # getinfo(self)
    # 플러그인 엔진의 주요 정보를 알려준다. ( 제작자, 버전, ... )
    # 리턴값 : 플러그인 엔진 정보
    # ----------------------------------------------------------------------------
    def getinfo(self): # 플러그인 엔진의 주요 정보
        info = dict() # 사전형 변수 선언

        info['author'] = 'Kei Choi' # 제작자
        info['version'] = '1.0' # 버전
        info['title'] = 'Dummy Scan Engine' # 엔진 설명
        info['kmd_name'] = 'dummy' # 엔진 파일 이름

        return info
