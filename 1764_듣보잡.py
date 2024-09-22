from sys import stdin
from collections import deque

n,m = stdin.readline().split() #n= 듣 / m = 보
n_set = set()
m_set = set()

for i in range(int(n) + int(m)):
    name = stdin.readline()
    if(i < int(n)):
        n_set.add(name)
    else:
        m_set.add(name)

# print(n_set)
# print(m_set) #디버깅

total = 0
ans = []
for i in n_set:
    if(i in m_set):
        total += 1
        ans.append(i)
    else:
        continue

ans.sort()
print(total,'\n',*ans,sep='')