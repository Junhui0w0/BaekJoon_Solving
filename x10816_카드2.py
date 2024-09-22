from sys import stdin
from collections import deque

n = int(stdin.readline())
n_set = deque(stdin.readline().split())

m = int(stdin.readline())
m_deque = deque(stdin.readline().split())

# print(n_set)
# print(m_deque) #디버깅

ans = deque()
for v in m_deque:
    if(v in n_set):
        ans.append(n_set.count(v))
    else:
        ans.append(0)

print(*ans)