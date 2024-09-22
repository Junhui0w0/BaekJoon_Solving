from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**6)

pc = int(stdin.readline().rstrip()) #PC 갯수
network = int(stdin.readline().rstrip()) #Network 연결 갯수

virus_route = []
is_go = [False] * (pc+1)
for i in range(network):
    data = list(map(int, stdin.readline().rstrip().split()))
    virus_route.append(data)
#print(virus_route) #디버깅


#바이러스는 반드시 1번 컴퓨터에서 시작
def dfs(start):
    for first, second in virus_route:
        if first == start:
            is_go[second] = True
            dfs(second)

dfs(1)

cnt = 0
for i in is_go:
    if i == True:
        cnt += 1
print(cnt)