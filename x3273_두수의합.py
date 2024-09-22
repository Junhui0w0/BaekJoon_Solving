from sys import stdin
from collections import deque

N = int(stdin.readline())
lst = deque(map(int, stdin.readline().rstrip().split()))
X = int(stdin.readline())

total = 0
i = 0
while(True):
    if((X - lst[i]) in lst):
        total += 1
        data = lst[i]
        lst.remove(data)
        lst.remove(X - data)
    else:
        i += 1
    
    if(i == 0):
        if(lst[0] == lst[-1]):
            break
    else:
        if(lst[i-1] == lst[-1]):
            break

print(total)