# -*- coding: utf-8 -*-
from random import *

count = 4
right = 1
num = randint(1, 20)
while count > 0:
    guess = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요 : " % count))
    if num == guess:
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." % right)
        break
    elif num > guess:
        print("Up")
        count -= 1
        right += 1

    elif num < guess:
        print("Down")
        count -= 1
        right += 1

    if count == 0:
        print("아쉽습니다. 정답은 %d 였습니다." % num)
