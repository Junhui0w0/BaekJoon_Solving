from sys import stdin

N = int(stdin.readline())
lst = []

for i in range(N):
    data = stdin.readline().split()
    coord = lst.append([int(data[1]), int(data[0])])

#print(lst) #디버깅  
lst.sort()

for value in lst:
    print(value[1], value[0])