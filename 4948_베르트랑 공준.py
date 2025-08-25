import sys
input = sys.stdin.readline

#입력
    #1. [...]: 소수를 구할 범위 (n+1~2n)

#실행
    #1. 입력의 마지막 값에는 0이 주어진다.

#출력
    #1. n보다 크고, 2n보다 작거나 같은 소수의 갯수를 출력한다.

while(True):
    n = int(input().rstrip())

    if n == 0:
        break

    #- 에라토스테네스의 체 활용
    lst = [True] * (2*n +1) #index=0~2n
    lst[0] = False 
    lst[1] = False #0과 1은 소수가 아님

    for i in range(2, int((2*n) ** 0.5)+1):
        for j in range(2*i, 2*n + 1, i):
            lst[j] = False

    print(lst[n+1:].count(True))
    # for i in range(n, len(lst)):
    #     if lst[i] == True and i % 2 == 0:
    #         print(i)