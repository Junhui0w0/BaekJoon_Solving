from sys import stdin
M, N = map(int, stdin.readline().split()) # M ~ N 사이의 소수 구하기

lst = [True] * (N+1) #index가 0 ~ N까지 (N+1개) 존재
lst[0] = False
lst[1] = False #0과 1은 소수가 아님.

for i in range(2, int(N**0.5)+1, 1): #2 ~ 제곱근N 까지
    if lst[i]:
        for j in range(i*2, N+1, i):
            lst[j] = False

for i in range(M,N+1):
    if lst[i]:
        print(i)