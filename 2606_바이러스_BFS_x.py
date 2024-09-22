from sys import stdin
from collections import deque

pc = int(stdin.readline().rstrip())
network = int(stdin.readline().rstrip())

virus_route = []
for i in range(network):
    data = list(map(int, stdin.readline().rstrip().split()))
    virus_route.append(data)
    
virused_pc = [False] * (pc+1)

q = deque()
q.append(1) #바이러스는 반드시 1번 컴퓨터에서 시작함
while(q):
    first = q.pop()
    for f,s in virus_route:
        if f == first:
            virused_pc[s] = True
            q.append(s)
        
        elif s == first:
            virused_pc[f] == True
            q.append(f)

total = 0
for i in virused_pc:
    if i == True:
        total += 1

print(total)


