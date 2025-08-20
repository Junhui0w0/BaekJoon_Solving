import sys
input = sys.stdin.readline
import heapq
import copy

#입력
    #1. N: 도시의 갯수
    #2. M: 버스의 갯수
    #3. [bus_start, bus_end, cost] (M개) -> bus_start: 버스의 출발 도시 / bus_end: 버스의 도착 도시 / cost: 비용
    #4. [start_city, end_city] -> start_city: 출발 도시 / end_city: 도착 도시

#실행 및 출력
    #1. 출발도시(start_city)에서 도착도시(end_city)까지 가는데 드는 최소 비용을 출력한다.

N = int(input())
M = int(input())

route_lst = [[] for _ in range(N+1)] #index=0~N -> 각 인덱스는 도시 번호를 나타냄
for _ in range(M):
    bus_start, bus_end, cost = map(int, input().rstrip().split())
    route_lst[bus_start].append((cost, bus_end)) #우선순위 정렬할 때 cost를 기준으로 정렬하기 편함

start_city, end_city = map(int, input().rstrip().split())

heap_lst = []
for cost, end in route_lst[start_city]:
    heapq.heappush(heap_lst, (cost, end)) #- heapq는 값을 넣는 순서에 따라 정렬을 달리함 -> 작은값부터 차례대로 정렬

MAX_DIST = float('INF')
dp_lst = [MAX_DIST] * (N+1) #index=0~N / start_city에서 각 index(도착도시)까지의 최소 거리 저장
dp_lst[start_city] = 0 #도착도시 to 도착도시 = 0
dp_lst[0] = 0 #0번 도시는 없음

while(heap_lst):
    cost, end = heapq.heappop(heap_lst)

    if dp_lst[end] < cost: #기존에 있던 루트보다 현재 루트로 가는 것의 비용이 큰 경우 -> 굳이 갈 필요 없음
            # 만약, 다음(next)로 가는 경우가 더 짧을 수 있으므로 등호(=) 삭제
        continue

    dp_lst[end] = cost

    for next_cost, next_end in route_lst[end]:
        total_cost = next_cost + cost

        if total_cost >= dp_lst[next_end]: #현재 저장된 비용보다 다음으로 진행하는 루트의 비용이 더 크거나 같은 경우 -> 굳이 진행 X
            continue

        dp_lst[next_end] = total_cost
        heapq.heappush(heap_lst, (total_cost, next_end)) 

print(dp_lst[end_city])