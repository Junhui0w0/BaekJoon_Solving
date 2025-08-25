import sys
input = sys.stdin.readline

#입력
    #1. N: 배열에 들어가는 데이터 갯수
    #2. [...] (N개): 배열에 들어가는 데이터(정수)

#실행
    #1. 배열에 들어가는 데이터는 임의로 순서를 바꿀 수 있다.

#출력
    #1. |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]| 가 최대가 되는 값을 출력한다.

N = int(input())
data_lst = list(map(int, input().rstrip().split()))
visited = [False] * N
max_v = -1

tmp = []
def DFS(cur_idx):
    global max_v

    if len(tmp) == N:
        total = 0

        for i in range(N-1):
            total += abs(tmp[i] - tmp[i+1])

        max_v = max(max_v, total)
        return True
    
    for i in range(N):
        if visited[i] == False:
            tmp.append(data_lst[i])
            visited[i] = True

            DFS(cur_idx)
            
            tmp.pop(-1)
            visited[i] = False

DFS(0)
print(max_v)