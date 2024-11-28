from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().rstrip().split()) #N=물품 갯수 / K=한번에 들 수 있는 무게

backpack_lst = []
for i in range(N):
    input_data = list(map(int, input().rstrip().split())) #무게(W) / 가치(V)
    backpack_lst.append(input_data)

# #BFS -> 시간초과 
# max_v = 0

# def BFS(cur_weight, cur_value, index):
#     global max_v
#     for i in range(index, N):
#         if visited[i] == True:
#             continue

#         if cur_weight + backpack_lst[i][0] <= K:
#             visited[i] = True
#             max_v = max(max_v, cur_value + backpack_lst[i][1])
#             BFS(cur_weight + backpack_lst[i][0], cur_value + backpack_lst[i][1], index)
#             visited[i] = False

#     return True

# for i in range(N):
#     visited = [False] * N
#     visited[i] = True
#     total = BFS(backpack_lst[i][0], backpack_lst[i][1], i)

# print(max_v)


#DP로 접근
#https://blog.naver.com/ndmns941/223384337943
#-> 글 그냥 무지성 읽기 반복 해
dp_lst = [[0]*(K+1) for i in range(N+1)]

for i in range(1, N+1): #i = 각 백팩에 들어있는 아이템 번호
    weight = backpack_lst[i-1][0]
    value = backpack_lst[i-1][1]

    for j in range(1, K+1):
        if j >= weight:
            dp_lst[i][j] = max(value + dp_lst[i-1][j-weight], dp_lst[i-1][j])
        else:
            dp_lst[i][j] = dp_lst[i-1][j]

print(dp_lst[-1][-1])