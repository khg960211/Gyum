# -*- coding: utf-8 -*-
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 인덱스와 원소 출력
# 코드를 입력하세요.
for i in range(len(numbers)):
    print(i, numbers[i])


# print 함수는 print(*objests, sep=' ', end='\n', file=sys.stdout, flush=False): 와 같이 정의되어 있다.
# 여기서 *objests가 있기 때문에 ',' 뒤에 다른 값을 써 주면 다른 값도 같이 출력된다.
# '*파라미터변수'는 ','를 이용하여 여러  값을 받아서 출력할 수 있다.
# sep=' '가 기본적으로 정해저 있어서 ','로 구분 된 값 사이에 공백이 포함되어 출력되고
# end='\n'으로 인해 print 함수 출력 후 한 줄 개행이 된다.
