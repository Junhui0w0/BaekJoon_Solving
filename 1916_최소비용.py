from collections import deque
import sys
input = sys.stdin.readline

city_num = int(input())
bus_num = int(input())
route_lst = [[] for _ in range(city_num+1)] # index = 0 ~ city_num까지

for i in range(bus_num):
    route_data = list(map(int, input().rstrip().split()))
    route_lst[route_data[0]].append((route_data[1], route_data[2]))


# print(route_lst)

start, end = int(input().split())
next_route = route_lst[start] #start 지점에서 시작해서 갈 수 있는 지점

#DFS 구현 -> Stack (후입선출)
max_cost = 999999

def DFS(lst, cur_cost=0):
    