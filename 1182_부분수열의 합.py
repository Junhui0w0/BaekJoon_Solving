import sys
input = sys.stdin.readline

N, S = map(int, input().rstrip().split())
number_lst = list(map(int, input().rstrip().split()))

tmp = []
cnt = 0

def DFS(index, length):
    global cnt

    if len(tmp) == length:
        if sum(tmp) == S:
            cnt += 1

        return True

    for idx in range(index, N):
        tmp.append(number_lst[idx])

        DFS(idx+1, length)

        tmp.pop(-1)

for length in range(1, N+1):
    DFS(0, length)

print(cnt)