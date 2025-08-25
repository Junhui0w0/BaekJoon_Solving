# from collections import deque
# import sys
# input = sys.stdin.readline

# #입력
#     #1. N, M -> N: 정점의 갯수 / M: 간선의 갯수
#     #2. [u, v] -> u & v: 간선의 양 끝점

# #실행
#     #1. 간선은 양방향이다.

# #출력
#     #1. 연결 요소의 갯수를 출력한다.

# N, M = map(int, input().rstrip().split())

# dp_lst = [i for i in range(N+1)] #index = 0 ~ N
# route_lst = [[] for _ in range(N+1)] #index= 0 ~ N

# for _ in range(M):
#     start, end = map(int, input().rstrip().split())
#     route_lst[start].append(end)
#     route_lst[start].sort(reverse=True)   

#     route_lst[end].append(start)
#     route_lst[start].sort(reverse=True)



# # print(route_lst)
# #- Union-Find AL를 활용해 같은 집합에 속해있는 가? 를 기반으로 문제 해결 가능할 듯

# def find_parent(lst, index):
#     if lst[index] != index:
#         lst[index] = find_parent(lst, lst[index])

#     return lst[index]

# def union(lst, indexA, indexB):
#     rootA = find_parent(lst, indexA)
#     rootB = find_parent(lst, indexB)

#     if rootA < rootB:
#         lst[rootB] = rootA
    
#     else:
#         lst[rootA] = rootB

# for route_index in range(1, N+1):
#     for end in route_lst[route_index]:
#         union(dp_lst, route_index, end)

# # print(dp_lst[1:])

# ans = set(dp_lst[1:])
# print(len(ans))



from collections import deque
import sys
input = sys.stdin.readline

#입력
    #1. N, M -> N: 정점의 갯수 / M: 간선의 갯수
    #2. [u, v] -> u & v: 간선의 양 끝점

#실행
    #1. 간선은 양방향이다.

#출력
    #1. 연결 요소의 갯수를 출력한다.


# print(route_lst)
#- Union-Find AL를 활용해 같은 집합에 속해있는 가? 를 기반으로 문제 해결 가능할 듯

def find_parent(lst, index):
    if lst[index] != index:
        lst[index] = find_parent(lst, lst[index])

    return lst[index]

def union(lst, indexA, indexB):
    rootA = find_parent(lst, indexA)
    rootB = find_parent(lst, indexB)

    if rootA < rootB:
        lst[rootB] = rootA
    
    else:
        lst[rootA] = rootB


N, M = map(int, input().rstrip().split())

dp_lst = [i for i in range(N+1)] #index = 0 ~ N

for _ in range(M):
    start, end = map(int, input().rstrip().split())
    union(dp_lst, start, end)

for i in range(1, N+1):
    dp_lst[i] = find_parent(dp_lst, i)

# print(dp_lst[1:])

ans = set(dp_lst[1:])
print(len(ans))

