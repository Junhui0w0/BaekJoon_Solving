import sys
input =sys.stdin.readline

#입력
    #1. N: 자릿수 

#실행
    #1. <0,1,2> 만을 사용할 수 있다.
    #2. 총 N자리의 숫자를 만들어야 한다.
    #3. 0으로 시작하는 숫자는 만들 수 없다.

#출력
    #1. <0,1,2>만을 가지고 만들 수 있는 N자리 3의 배수의 갯수를 출력한다.

#- 3의 배수 판별 -> 모든 자릿수 합 % 3 == 0

N = int(input())
cnt = 0

def DFS(start_value):
    global cnt
    if len(tmp) == N:
        total = sum(tmp)

        if total % 3 == 0:
            cnt += 1

        return True
    
    for i in range(0, 3): #i = 0 ~ 2
        tmp.append(i)
        DFS(start_value)
        tmp.pop(-1)

tmp = [1]
DFS(1)

tmp = [2]
DFS(2)

print(cnt)