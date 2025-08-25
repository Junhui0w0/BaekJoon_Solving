import sys
input = sys.stdin.readline

#입력
    #1. [N, ...] -> N: 집합에 사용될 원소의 갯수 / ... : 집합에 사용되는 숫자
        #1-1. 입렵되는 숫자는 항상 오름차순으로 정렬되어 있다.
        #1-2. 단, 0이 들어올 경우 입력은 종료된다.

#실행
    #1. 로또 번호는 총 숫자 6개로 구성되어 있다.

#출력
    #1. 로또 번호로 사용가능한 모든 경우의 수를 출력한다.

def DFS(cur_idx, n):
    if len(tmp) == 6:
        print(*tmp)
        return True
    
    for i in range(cur_idx, n):
        tmp.append(data_lst[i])
        DFS(i+1, n)
        tmp.pop(-1)

    return False
    

while(True):
    number_lst = list(map(int, input().rstrip().split()))

    if number_lst[0] == 0:
        break

    length = number_lst[0] #원소의 총 갯수
    data_lst = number_lst[1:] #로또 번호에 사용 가능한 숫자

    tmp = []
    DFS(0, length)
    print()