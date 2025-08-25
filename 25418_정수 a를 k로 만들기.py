import sys
input=sys.stdin.readline

#입력
    #1. A, K -> A: 시작값 / K: 타겟값

#실행
    #1. 사용할 수 있는 연산은 아래와 같다.
        #1-1. 정수 A에 1을 더한다.
        #1-2. 정수 A에 2를 곱한다.

#출력
    #1. A를 K로 만들기 위해 필요한 최소 연산 횟수를 출력한다.

A, K = map(int, input().rstrip().split())

MAX_V = float('INF')
dp_lst = [MAX_V] * (K+1) #0~K
dp_lst[A] = 0

for i in range(A+1, K+1): #A+1 ~ K
    dp_lst[i] = min(dp_lst[i], dp_lst[i-1] + 1)

    if i % 2 == 0 and i // 2 >= A:
        dp_lst[i] = min(dp_lst[i], dp_lst[i//2] + 1)

print(dp_lst[-1])