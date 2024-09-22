from sys import stdin
from collections import Counter

n = int(stdin.readline().rstrip())

lst = []
for i in range(n):
    data = int(stdin.readline().rstrip())
    lst.append(data)

c = Counter(lst)
c = sorted(c.items(), key=lambda x : x[1], reverse=True)
#print(c) #디버깅

max_counter = []
max = c[0][1]
#print("최대 빈도수: ",max) #디버깅
for i in range(len(c)):
    if(c[i][1] != max):
        break
    else:
        max_counter.append(c[i][0])

max_counter.sort()
#print(max_counter) #디버깅
print(max_counter[0])