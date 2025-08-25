import sys
input = sys.stdin.readline

#입력
    #1. N: 연산에 사용할 숫자의 갯수 
    #2. [...(N개)]: 연산에 사용할 각 숫자
    #3. [plus, minus, multi, div]: 연산자 갯수

#실행
    #1. 모든 수의 사이에는 연산자를 한 개 끼워넣어야 한다. (연산자가 남을 수 있다.)
    #2. 주어진 수의 순서는 변경할 수 없다.
    #3. 연산자 우선순위는 무시하고, 왼쪽부터 차례대로 계산한다.
    #4. 음수를 양수로 나눌 경우 음수를 양수르 치환 후 몫을 계산하여 다시 음수로 치환한다.

#출력
    #1. 만들 수 있는 결과값의 최소값과 최대값을 출력한다.

N = int(input()) #2이상 11이하
number_lst = list(map(int, input().rstrip().split())) #각 숫자는 2이상 100이하

oper_lst= list(map(int, input().rstrip().split())) #<index> 0: 합 / 1: 차 / 2: 곱 / 3: 나눗셈 갯수
for idx in range(4): #index=0~3
    oper_lst[idx] = min(oper_lst[idx], N-1) #한 종류의 연산자 갯수가 넘치는 경우 방지

min_v = 1000000000
max_v = -1000000000

def operation(cur_total, oper_idx, next_value):
    if oper_idx == 0: #합
        cur_total += next_value

    elif oper_idx == 1: #차
        cur_total = cur_total - next_value

    elif oper_idx == 2: #곱
        cur_total = cur_total * next_value

    elif oper_idx == 3: #나눗셈
        if cur_total < 0: #현 합계가 음수인경우
            cur_total = -1 * cur_total
            cur_total = (cur_total // next_value) * -1

        else:
            cur_total = cur_total // next_value

    return cur_total

tmp = [] #oper 경우의 수를 담을 lst
def DFS():
    global min_v, max_v

    if len(tmp) == N-1: #연산자의 갯수가 N-1개 일 때 끝나
        cur_total = number_lst[0]

        for i in range(N-1):
            cur_total = operation(cur_total, tmp[i], number_lst[i+1])

        min_v = min(min_v, cur_total)
        max_v = max(max_v, cur_total)

        return True
    
    for idx in range(4):
        if oper_lst[idx] == 0: #i번째 operation 갯수가 0개면 연산자 끼워넣을 수 없음
            continue

        tmp.append(idx)
        oper_lst[idx] = oper_lst[idx]-1
        DFS()
        tmp.pop(-1)
        oper_lst[idx] = oper_lst[idx]+1

DFS()
print(max_v)
print(min_v)