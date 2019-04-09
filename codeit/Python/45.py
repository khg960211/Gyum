# -*- coding: utf-8 -*-
# BFS(Breadth-First Search) 알고리즘을 이용한 두 지하철역 사이의 최단 경로를 계산하는 프로그램

# -*- coding: utf-8 -*-
# BFS(Breadth-First Search) 알고리즘을 이용한 두 지하철역 사이의 최단 경로를 계산하는 프로그램
from collections import deque
import io

# 지하철역 클래스
class Station:
    def __init__(self, name):
        self.name = name
        # 이웃 역들을 담고 있는 리스트
        self.neighbors = []

    def add_connection(self, another_station):
        self.neighbors.append(another_station)
        another_station.neighbors.append(self)

# Breadth-First Search 알고리즘
def bfs(start, goal):

    previous = {}
    queue = deque()
    current = None

    previous[start] = None
    queue.append(start)

    # 아직 보지 않은 역이 있고, 도착역을 찾지 않았을 경우 반복
    while len(queue) > 0 and current != goal:
        current = queue.popleft()

        for neighbor in current.neighbors:
            if neighbor not in previous.keys():
                queue.append(neighbor)
                previous[neighbor] = current

        # 만약 current가 goal이면 경로를 만들어서 리턴
        if current == goal:
            path = []
            x = goal

            while previous[x] != None:
                x = previous[x]
                path.append(x)

            return path

    # current가 goal이 아니면 None을 리턴
    return None


# 파일 읽기
stations = {}
in_file = open('stations.txt')

for line in in_file:
    previous_station = None
    station_name = line.strip().split(" - ")

    for i in range(len(station_name)):
        # 새로운 역이라면
        station_name[i] = station_name[i].strip()
        if station_name[i] not in stations.keys():
            station = Station(station_name[i])
            stations[station_name[i]] = station
        # 아까 저장했던 역이라면
        else:
            station = stations[station_name[i]]

        # 이전 역이 있다면
        if previous_station != None:
            station.add_connection(previous_station)
        # 맨 처음 역이라면
        previous_station = station


# 테스트
start_name = "당산"
goal_name = "건대입구"

start = stations[start_name]
goal = stations[goal_name]

path = bfs(start, goal)
for station in path:
    print(station.name)
