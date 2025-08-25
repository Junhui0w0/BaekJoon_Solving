import sys
input = sys.stdin.readline

#입력
    #1. N: 테스트케이스 갯수
    #2. [...] (N줄): 입력 데이터

#실행
    #1. 입력 데이터는 '(' 또는 ')' 로만 구성되어 있다.
    #2. '()' 는 Valid PS (VPS) 로써 올바른 괄호 문자열 이라고 부른다.

#출력
    #1. 주어진 입력데이터가 올바른 괄호 문자열로 구성되어 있다면 YES를 그렇지 않으면 NO를 출력한다.

N = int(input())

for _ in range(N):
    input_data = list(str(input().rstrip()))
    stack_lst = [input_data[0]]
    # print(stack_lst)

    for data in input_data[1:]:
        stack_lst.append(data)

        if len(stack_lst) <= 1:
            continue

        if stack_lst[-2] == '(' and stack_lst[-1] == ')':
            stack_lst.pop(-2)
            stack_lst.pop(-1)

    if len(stack_lst) == 0:
        print('YES')

    else:
        print('NO')