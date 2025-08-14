import sys
input = sys.stdin.readline

#입력
    #1. n: 공약수를 구해야하는 자연수의 갯수 (2 또는 3)
    #2. [...] (n개): 공약수를 구해야하는 자연수

#실행 및 출력
    #1. 자연수들의 공약수를 작은 값대로 출력한다.

N = int(input())

answer = ''

if N == 2:
    a, b = list(map(int, input().rstrip().split()))
    min_v = min(a,b)

    for i in range(1, min_v+1):
        if a % i == 0 and b % i == 0:
            answer += str(i) + '\n'

else:
    a,b,c = list(map(int, input().rstrip().split()))
    min_v = min(a,b,c)

    for i in range(1, min_v+1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            answer += str(i) + '\n'

print(answer)