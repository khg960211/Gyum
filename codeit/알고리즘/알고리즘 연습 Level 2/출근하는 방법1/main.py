# 영훈이는 출근할 때 계단을 통해 사무실로 가는데요. 급할 때는 두 계단씩 올라가고 여유 있을 때는 한 계단씩 올라 갑니다.
# 어느 날 문득, 호기심이 생겼습니다. 한 계단 또는 두 계단씩 올라가서 끝까지 올라가는 방법은 총 몇 가지가 있을까요?
# 계단 4개를 올라간다고 가정하면, 이런 방법들이 있습니다.
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# 총 5개 방법이 있네요.
# 함수 staircase는 파라미터로 계단 수 n을 받고, 올라갈 수 있는 방법의 수를 효율적으로 찾아서 리턴합니다.

def staircase(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a

# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
