# -*- coding: utf-8 -*-
# 책 173쪽

import os
import sys
import k2kmdfile

if __name__ == '__main__':
    #---------------------------------------------------------------------------
    # 인자값을 체크한다.
    #---------------------------------------------------------------------------
    if len(sys.argv) != 2:
        print('Usage : kmake2.py [python source]')
        exit()

    k2kmdfile.make(sys.argv[1], True)
