from sys import stdin

N = int(stdin.readline().rstrip())

s = ''
for i in range(1,N+1):
    s = s + str(i)

print(len(s))