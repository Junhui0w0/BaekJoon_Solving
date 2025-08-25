from collections import deque
import sys
input = sys.stdin.readline

#입력
    #1. N, K -> N: 운동 키트 갯수 / K: 하루마다 빠지는 중량
    #2. [...] (N개): 각 키트 수행 시 중량 증가량

#실행
    #1. 각 일마다 중량은 500 이상이어야 한다.

#출력
    #1. N일 동안 N개의 운동 키트를 사용하는 모든 경우 중에서, 운동 기간동안 항상 중량이 500 이상이 되도록 하는 경우의 수를 출력한다.

N, K = map(int, input().rstrip().split())
weight_lst = list(map(int, input().rstrip().split()))
cnt = 0 #가능한 경우의 수

def DFS(cur_weight):
    global cnt

    if len(tmp) == N: #모든 운동 키트를 사용했는가?
        if cur_weight >= 500:
            cnt += 1
            
        return True

    if cur_weight < 500: #모든 운동 키트를 사용하지 않았는데, weight가 500 미만이다? -> 해당 걍우의 수는 불가능
        return False
    
    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            tmp.append(i)

            DFS(cur_weight + (weight_lst[i] - K))

            visited[i] = False
            tmp.pop(-1)


for idx in range(N):
    visited = [False] * N #현재 키트를 사용했는가 ?
    visited[idx] = True #현 idx는 사용중
    
    tmp = [idx] #현재 사용하고 있는 중량 idx
    DFS(500 + (weight_lst[idx]-K))

print(cnt)