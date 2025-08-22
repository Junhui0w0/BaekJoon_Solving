import sys
input = sys.stdin.readline

#입력
    #1. N: 토끼가 지불해야하는 금액

#실행
    #1. 토끼가 사용할 수 있는 동전의 금액은 1원, 2원, 5원, 7원 총 4종류만 있다.
    #2. 4종류의 동전은 무한대로 사용할 수 있다.
    #3. 최소한의 동전만을 사용해서 N을 맞춰야 합법이다.

#출력
    #1. 토끼가 합법적으로 낼 수 있는 동전의 갯수를 출력한다.

N = int(input())
MAX_V = float('INF')
coin_lst = [1, 2, 5, 7]

if N == 0:
    print(0)
    
elif N <= 7:
    dp_lst = [MAX_V] * (7+1) #0~7
    
    for coin in coin_lst:
        dp_lst[coin] = 1 #자기자신을 만들 수 있는 최소횟수 = 1

    for i in range(1, 7+1):
        if dp_lst[i] == MAX_V:
            
            for coin in coin_lst:
                value = i - coin

                if value > 0: #양수라면 만들 수 있음
                    dp_lst[i] = min(dp_lst[i], dp_lst[value] + 1)

    print(dp_lst[N])

else:
    dp_lst = [MAX_V] * (N+1) #0~N

    for coin in coin_lst:
        dp_lst[coin] = 1

    for i in range(1, N+1): #1~N
        if dp_lst[i] == MAX_V:

            for coin in coin_lst:
                value = i - coin

                if value > 0:
                    dp_lst[i] = min(dp_lst[i], dp_lst[value]+1)

    print(dp_lst[N])