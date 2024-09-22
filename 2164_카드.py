from sys import stdin
from collections import deque

N = int(stdin.readline()) #1 ~ N 카드

d = deque()
for i in range(1,N+1):
    d.append(i)

print(d) #디버깅

while(True):
    if(len(d) == 1):
        break
    else:
        d.popleft() #첫번째 값 제거
        d.append(d[0]) #제거된 이후 첫번째 값 뒤로 이동
        d.popleft()
    
print(d[0])