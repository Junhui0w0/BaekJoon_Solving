from sys import stdin

N = int(stdin.readline()) #입력받을 데이터 갯수 입력
lst = list()

for i in range(N):
    lst.append(int(stdin.readline()))

lst.sort()

for i in lst:
    print(i)