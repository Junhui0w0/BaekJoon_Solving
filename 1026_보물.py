from sys import stdin
from collections import deque

N = int(stdin.readline())

n_lst = list(map(int, stdin.readline().split()))
m_lst = list(map(int, stdin.readline().split()))

n_lst.sort()
m_lst.sort(reverse=True)

total = 0
for i in range(N):
    total = total + (n_lst[i] * m_lst[i])

print(total)