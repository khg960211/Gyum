# -*- coding: utf-8 -*-
from collections import deque

# 지하철역 클래스
class Station:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_connection(self, another_station):
        self.neighbors.append(another_station)
        another_station.neighbors.append(self)


# Breadth-First Search 알고리즘
def bfs(start, goal):
    # 변수 정의
    previous = {}
    queue = deque()
    current = None

    # 초기 설정
    previous[start] = None
    queue.append(start)

    # 탐색
    while len(queue) > 0 and current != goal:
        current = queue.popleft()

        for neighbor in current.neighbors:
            if neighbor not in previous.keys():
                queue.append(neighbor)
                previous[neighbor] = current

    # 길이 있으면 경로를 만들어서 리턴
    if current == goal:
        path = [goal]
        x = goal

        while previous[x] != None:
            x = previous[x]
            path.append(x)

        return path

    # 길이 없으면 None 리턴
    return None


# 파일 읽기
stations = {}
in_file = open('stations.txt')

for line in in_file:
    previous_station = None
    data = line.strip().split("-")

    for name in data:
        station_name = name.strip()
        if station_name not in stations.keys():
            current_station = Station(station_name)
            stations[station_name] = current_station
        else:
            current_station = stations[station_name]

        if previous_station != None:
            current_station.add_connection(previous_station)

        previous_station = current_station

in_file.close()

# 테스트
start_name = "당산"
goal_name = "건대입구"

start = stations[start_name]
goal = stations[goal_name]

path = bfs(start, goal)
path.reverse()
for station in path:
    print(station.name)
