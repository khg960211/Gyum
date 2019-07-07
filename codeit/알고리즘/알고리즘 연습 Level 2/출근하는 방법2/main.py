# 시간 복잡도
# stairs가 n, possible_steps의 길이가 m이라고 할 때, staircase 함수는 n에 비례하는 반복문 안에 m에 비례하는 반복문 하나가 있죠?
# 
# 그렇기 때문에 이 함수의 시간 복잡도는 O(mn)입니다.

# 높이 n개의 계단을 올라가는 방법을 리턴한다
def staircase(stairs, possible_steps):
    # 계단 높이가 0 이거나 1 이면 올라가는 방법은 한 가지밖에 없다
    number_of_ways = [1, 1]

    # 이 변수들을 업데이트 해주며 n 번째 계단을 오르는 방법의 수를 구한다.
    for height in range(2, stairs + 1):
        number_of_ways.append(0)

        for step in possible_steps:
            # 음수 계단 수는 존재하지 않기 때문에 무시합니다
            if height - step >= 0:
                number_of_ways[height] += number_of_ways[height - step]

    return number_of_ways[stairs]

print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))
