from sys import stdin
from collections import Counter,deque

N= int(stdin.readline()) #입력받을 데이터 개수
lst = [0] * N

for i in range(N):
    data = stdin.readline().rstrip()
    lst[i] = int(data)

lst.sort()
#print(sum(lst)) #디버깅

#산술평균
#print('산술평균', end='') #디버깅
if(sum(lst)/N > 0): #평균이 양수
    print(round(sum(lst)/N)) 
else: #평균이 음수 -> -3.4 (-4) // -3.5 (-3) -> 반대임?
    if(int(round(sum(lst)/N,2)) - round(sum(lst)/N,2) >= 0.5 ):
        print(int(sum(lst)/N) - 1)
    else:
        print(int(sum(lst)/N))

#중앙값
#print('중앙값', end='') #디버깅
print(lst[int((N-1)/2)])

#최빈값
#print('최빈값', end='') #디버깅
c = Counter(lst)
c = sorted(c.items(), key=lambda x : x[1], reverse=True)
#print(c) #디버깅
max_value = c[0][1]

total = 0
for i in range(len(c)):
    if(c[i][1] != max_value):
        break
    else:
        total += 1

if(total >= 2):
    print(c[1][0])
else:
    print(c[0][0])

#범위
#print('범위', end='') #디버깅
print(lst[-1] - lst[0])