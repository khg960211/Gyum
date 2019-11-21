# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, 'D:\\Gyum\Project\engine\kavcore')
import k2engine

# listvirus의 콜백 함수
def listvirus_callback(plugin_name, vnames):
    for vname in vnames:
        print '%-50s [%s.kmd]' % (vname, plugin_name)

k2 = k2engine.Engine(debug=True)
# k2.set_plugins('plugins') # 플러그인 엔진 경로를 정의한다.
if k2.set_plugins('plugins'): # 성공?
    kav = k2.create_instance() # 백신 엔진 인스턴스를 생성
    if kav:
        print '[*] Success : create_instance'

        ret = kav.init() # 플러그인 엔진 초기화
        info = kav.getinfo() # 플러그인 엔진의 정보를 얻는다.

        vlist = kav.listvirus(listvirus_callback) # 플러그인의 바이러스 목록을 출력한다.

        print '[*] Used Callback        : %d' % len(vlist)

        vlist = kav.listvirus() # 플러그인의 바이러스 목록을 얻는다.
        print '[*] Not used Callback : %d' % len(vlist)

        ret, vname, mid, eid = kav.scan('eicar.txt')
        if ret:
            kav.disinfect('eicar.txt', mid, eid)

        kav.uninit() # 플러그인 엔진 종료
