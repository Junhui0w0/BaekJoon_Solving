from sys import stdin
M,N = map(int, stdin.readline().split()) #M 이상 N 이하 소수 구하기
lst = [True] * (N+1) #0 ~ N까지 True로 채워넣은 LIST
lst[0] = False
lst[1] = False # 0과 1은 소수가 아님 

for i in range(2, int(N**0.5) + 1): #2 ~ N의 제곱근 까지 반복문
    if lst[i]:
        for k in range(2*i, N+1, i):
            lst[k] = False

for i in range(M, N+1):
    if lst[i]:
        print(i)