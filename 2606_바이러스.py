from sys import stdin
from collections import deque

pc = int(stdin.readline().rstrip()) #컴퓨터 갯수
line = int(stdin.readline().rstrip()) #경로 갯수

virus_route = []
for _ in range(line):
    data = list(map(int, stdin.readline().rstrip().split())) #x - y 가 양방향으로 바이러스 연결되어있음
    virus_route.append(data)

#print(virus_route) #디버깅

is_go = [False] * (pc + 1) #해당 지점에 갔음을 표시

q = deque()
q.append(1) #바이러스 시작 = 1번 PC

while(q):
    start = q.pop()
    for first, second in virus_route:
        if first == start:
            if is_go[second] == False:
                q.append(second)
                is_go[second] = True
        elif second == start: #양방향이기에 second와 first 둘 다 비교
            if is_go[first] == False:
                q.append(first)
                is_go[first] = True

is_go[1] = False

cnt = 0
for i in is_go:
    if i == True:
        cnt += 1

print(cnt)