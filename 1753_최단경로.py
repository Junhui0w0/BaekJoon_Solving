import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int, input().rstrip().split()) #V=정점 / E=간선
# print(f'V, E = {V}, {E}')

min_route_lst = [999999 for i in range(V+1)] #index = 0 ~ V // 출력 -> 1 ~ V -> for i in range(1, V+1)
# print(min_route_lst)

start_point = int(input().rstrip()) #시작점
min_route_lst[start_point] = 0 #시작점은 해당 지점까지 거리가 0

arrival_and_weight_lst = [[] for i in range(V+1)] #index=출발지 , [a,b] -> a=도착지 / b=가중치 

for i in range(E):
    u,v,w = map(int, input().rstrip().split()) #출발, 도착, 가중치

    if v == start_point: #도착지가 시작점과 동일한 경우 패스
        continue

    arrival_and_weight_lst[u].append((v,w))

# print(arrival_and_weight_lst)

#1. 출발지로 시작해서 도착지의 가중치를 우선 반영(min_route_lst[도착지] = 가중치)
    #1-1. 뽑은 (도착지, 가중치) -> 함수()

def DFS(start, cur_weight):

    if arrival_and_weight_lst[start] == []: #비어있다? 그럼 다음으로 넘어갈 노드가 없다는 것
        #즉, 현재 노드가 끝 이라는 것 - 업데이트1
        if cur_weight < min_route_lst[start]:
            min_route_lst[start] = cur_weight
        
        return True #끝내야지 없는데
    
    #만약 비어있지 않아? 어쨋든 가중치 업데이트는 진행
    if cur_weight < min_route_lst[start]:
        min_route_lst[start] = cur_weight #업데이트2

    for arrival, weight in arrival_and_weight_lst[start]:
        DFS(arrival, weight+cur_weight)

    return True

    # print('debug')

    
lst = arrival_and_weight_lst[start_point] #[(a,b), (c,d)...]
for arrival, weight in lst: #첫 시작이니까 상관없을듯? (이전 가중치가 없으니)
    # min_route_lst[arrival] = weight #가중치 업데이트 
    DFS(arrival, weight) # 도착지가 출발지가 됨

for i in range(1, V+1):
    if min_route_lst[i] == 999999:
        print('INF')
        continue
    print(min_route_lst[i])