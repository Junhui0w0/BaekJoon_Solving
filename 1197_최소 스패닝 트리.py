#- 크루스칼 AL
import sys
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#입력
    #1. V, E -> V: 정점의 갯수 / E: 간선의 갯수
    #2. [Start, End, Cost(E개)] -> Start: 간선의 시작점 / End: 간선의 끝점 / Cost: 간선의 가중치 값

#실행
    #1. 간선은 양방향 이동이 가능하다.

#출력
    #1. 주어진 그래프의 모든 정점을 연결하는 부분 그래프 중 가중치 합이 최소인 것을 출력한다.

V, E = map(int, input().rstrip().split())

route_lst = []
for _ in range(E):
    start, end, cost = map(int, input().rstrip().split())
    route_lst.append((cost, start, end))

route_lst.sort() #-> cost 기준으로 우선 정렬

def find_parent(lst, index):
    if lst[index] != index:
        lst[index] = find_parent(lst, lst[index])

    return lst[index]

def union_parent(lst, index_a, index_b):
    root_a = find_parent(lst, index_a)
    root_b = find_parent(lst, index_b)

    if root_a < root_b:
        lst[root_b] = root_a

    else:
        lst[root_a] = root_b

    return True

parent_lst = [i for i in range(V+1)] #0~V
total = 0

for cost, start, end in route_lst:
    start_parent = find_parent(parent_lst, start) #- cost를 기준으로 정렬해두었기 때문에 가중치가 작은 것부터 계산 가능
    end_parent = find_parent(parent_lst, end)

    if start_parent != end_parent: #서로의 부모가 다르다면 -> 합칠 수 있음 (싸이클이 안생기기 때문)
        union_parent(parent_lst, start, end)
        total += cost

print(total)