from sys import stdin

data = list(stdin.readline()) #데이터 입력
data.sort(reverse=True)

print(*data,sep='',end='')