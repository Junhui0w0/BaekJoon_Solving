from sys import stdin
import math

n, m = list(map(int, stdin.readline().split()))

#소수는 무조건 홀수 & 제곱수가 아니면 됨
if(n % 2== 0): #짝수
    n += 1

ans = ''
for i in range(n, m+1, 2): #n ~ m 까지 반복
    sq = len((str(math.sqrt(i)).split('.'))[1])
    #print(sq)
    if(sq != 1):
        ans = ans + str(i) + '\n'
    else:
        continue

print(ans)