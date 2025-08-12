# import sys
# from collections import deque
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# V, E = map(int, input().rstrip().split()) #V=정점 / E=간선
# # print(f'V, E = {V}, {E}')

# min_route_lst = [999999 for i in range(V+1)] #index = 0 ~ V // 출력 -> 1 ~ V -> for i in range(1, V+1)
# # print(min_route_lst)

# start_point = int(input().rstrip()) #시작점
# min_route_lst[start_point] = 0 #시작점은 해당 지점까지 거리가 0

# arrival_and_weight_lst = [[] for i in range(V+1)] #index=출발지 , [a,b] -> a=도착지 / b=가중치 
# is_visited = [[] for i in range(V+1)]

# for i in range(E):
#     u,v,w = map(int, input().rstrip().split()) #출발, 도착, 가중치

#     if v == start_point: #도착지가 시작점과 동일한 경우 패스
#         continue

#     arrival_and_weight_lst[u].append((v,w))
#     is_visited[u].append(False)

# # print(arrival_and_weight_lst)

# #1. 출발지로 시작해서 도착지의 가중치를 우선 반영(min_route_lst[도착지] = 가중치)
#     #1-1. 뽑은 (도착지, 가중치) -> 함수()

# def DFS(start, cur_weight, cur_idx):
#     if cur_weight < min_route_lst[start]:
#         min_route_lst[start] = cur_weight #업데이트1

#     #오버 했을 경우
#     if cur_idx >= len(is_visited[start]):
#         return True
    
#     #이미 방문한 곳인 경우
#     if is_visited[start][cur_idx] == True:
#         return True
    
#     is_visited[start][cur_idx] = True

#     idx2= 0 
#     for arrival, weight in arrival_and_weight_lst[start]:
#         DFS(arrival, weight+cur_weight, idx2)
#         is_visited[start][cur_idx] = False
#         idx2 += 1

#     return True

#     # print('debug')


# idx2 = 0
# lst = arrival_and_weight_lst[start_point] #[(a,b), (c,d)...]
# for arrival, weight in lst: #첫 시작이니까 상관없을듯? (이전 가중치가 없으니)
#     # min_route_lst[arrival] = weight #가중치 업데이트 
#     is_visited[start_point][idx2] = True
#     DFS(arrival, weight, 0) # 도착지가 출발지가 됨
#     idx2 += 1

# for i in range(1, V+1):
#     if min_route_lst[i] == 999999:
#         print('INF')
#         continue
#     print(min_route_lst[i])


import heapq
import sys
input = sys.stdin.readline

#입력
    #1. V, E -> V: 정점의 갯수 / E: 간선의 갯수
    #2. K: 시작 정점
    #3. [u, v, w] (E줄) -> u: 시작 노드 / v: 도착 노드 / w: 가중치(비용)

#실행
    #1. 시작 지점은 반드시 K 이다.
    #2. 간선은 u에서 v로만 갈 수 있으며, 서로 다른 두 정점 사이에 여러개의 간선이 존재할 수 있다.
    #3. 가중치 값은 10 이하의 자연수 이다.

#출력
    #1. 시작지점(K)에서 각 정점으로 가는데 필요한 최소 비용을 순서대로 출력한다.
        #1-1. 단, 시작점 자신은 0으로 출력하며, 경로가 존재하지 않는 경우 INF를 출력한다.

V, E = map(int, input().rstrip().split())
K = int(input())
MAX_V = float('INF')

route_lst = [[] for _ in range(V+1)] #index = 0 ~ V
    # 이때, index는 출발도시, 해당 index안에 있는 값들은 비용, 도착도시
    # cost를 먼저 삽입하는 이유는 우선순위큐(heapq)에 삽입하는 값의 순서에 따라 우선순위가 달라짐

tmp = []
# heapq.heappush(tmp, (0, K))

for _ in range(E):
    start, end, cost = map(int, input().rstrip().split())
    route_lst[start].append((cost, end))

    if start == K:
        heapq.heappush(tmp, (cost, end))

dp_lst = [MAX_V] * (V+1) #index = 0 ~ V
dp_lst[K] = 0 #자기자신은 0

while(tmp):
    cost, end = heapq.heappop(tmp) #우선순위큐로 추출 -> cost값이 작은 것부터 추출

    if dp_lst[end] < cost: #새로 가는 경로가 더 비효율적(가중치가 더 큼)인 경우 -> 그 경로로 갈 필요 없음
        continue

    dp_lst[end] = cost

    for next_cost, next_end in route_lst[end]:
        total_cost = cost + next_cost

        if total_cost < dp_lst[next_end]:
            dp_lst[next_end] = total_cost
            heapq.heappush(tmp, (total_cost, next_end))

for cost in dp_lst[1:]:
    if cost == MAX_V:
        print('INF')

    else:
        print(cost)