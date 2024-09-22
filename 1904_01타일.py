from sys import stdin
N = int(stdin.readline())

a = 0
while(True):
    if(2 ** a == N):
        break
    a += 1

print(a)