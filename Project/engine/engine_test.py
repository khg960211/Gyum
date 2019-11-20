# -*- coding: utf-8 -*-
import os
import sys
from kavcore import k2engine

k2 = k2engine.Engine(debug=True)
k2.set_plugins('plugins') # 플러그인 엔진 경로를 정의한다.
