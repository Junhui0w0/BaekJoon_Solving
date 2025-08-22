import sys
input = sys.stdin.readline

#입력
    #1. n: 함수에 집어넣을 인자값

#실행 및 출력
    #1. 피보나치 함수에 인자 n을 넣을 때 fibonacci 함수가 호출되는 횟수를 출력한다.

n = int(input())
if n == 0 or n == 1:
    print(1)

else:
    dp_lst = [1] * (n+1) #0~n
    
    for i in range(2, n+1):
        dp_lst[i] = (dp_lst[i-2] + dp_lst[i-1] + 1) % 1000000007

    print(dp_lst[-1])