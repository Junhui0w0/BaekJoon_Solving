import sys
input = sys.stdin.readline

#입력
    #1. n, m -> n: 행의 갯수 / m: 열의 갯수

#실행 및 출력
    #1. 좌측 상단(1,1)에서 우측 하단(n,m)에 도달할 수 있는 경우의 수 10^9 + 7로 나눈 나머지를 출력한다.

n, m = map(int, input().rstrip().split())

dp_lst = [([1] * m) for i in range(n)]

for i in range(1, n):
    for j in range(1, m):
        dp_lst[i][j] = (dp_lst[i-1][j] + dp_lst[i-1][j-1] + dp_lst[i][j-1]) % (10**9 + 7)

print(dp_lst[-1][-1])


#==============================================
# DP = Dynamic Programming = 동적 프로그래밍
# 계산했던 문제를 반복하지 않고 메모리에 기록해두어 필요할 때 꺼내 써 시간을 단축시키는 것 == 메모이제이션 기법
# 점화식 (N<i> = N<i-1> + M<i> 와 같은 형식) 을 세운 뒤 코드를 작성하면 편함