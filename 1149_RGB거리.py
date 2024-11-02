import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque

N = int(input().rstrip()) #집의 갯수
lst = []
for i in range(N):
    input_data = list(map(int, input().rstrip().split()))
    lst.append(input_data)

dp_lst = [[0,0,0] for i in range(N)]

for i in range(3):
    dp_lst[0][i] = lst[0][i] #초기값 지정

for i in range(1, N):
    for j in range(3):
        min_cost = 1000000
        for v in range(3):
            if j == v:
                continue #동일 열은 제외
            
            if dp_lst[i-1][v] < min_cost:
                min_cost = dp_lst[i-1][v] #직전까지의 누적합

            dp_lst[i][j] = min_cost + lst[i][j]

print(min(dp_lst[N-1]))