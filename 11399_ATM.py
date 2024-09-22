from sys import stdin

N = int(stdin.readline())

time_lst = list(map(int,stdin.readline().split()))
time_lst.sort()


total = 0
data = 0

for i in time_lst:
    total = total + i
    data = data + total

print(data)