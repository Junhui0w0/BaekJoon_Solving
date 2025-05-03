from collections import deque
import sys
input = sys.stdin.readline

def AC_func(method_lst, convert_data_lst, length):
    cur_status = 1 #1은 정방향, -1은 역방향
    for method in method_lst:
        if method == 'R':
            cur_status = cur_status * -1

        elif method == 'D':
            if length <= 0:            
                return 'error'
            
            length -= 1
            
            if cur_status == 1: #정방향 이라면
                convert_data_lst.pop(0)
            elif cur_status == -1: #역방향
                convert_data_lst.pop(-1)

    #에러 없이 수행 완료시
    if cur_status == 1: #정방향
        return convert_data_lst
    elif cur_status == -1:
        convert_data_lst.reverse()
        return convert_data_lst



loop = int(input()) #총 반복 횟수

for i in range(loop):
    method_lst = list(input().rstrip()) #R=뒤집기 / D=삭제
    data_len = int(input()) #데이터 갯수

    if data_len == 0:
        input_data = input().rstrip() #입력 데이터 -> [1, 2, 10] 형식
        if 'D' in method_lst:
            print('error')
            continue
        else:
            print('[]')
            continue
    
    input_data = input().rstrip() #입력 데이터 -> [1, 2, 10] 형식
    input_data = input_data.replace('[','')
    input_data = input_data.replace(']','')
    input_data = list(map(int, input_data.split(',')))

    # print(input_data)

    #method 수행
    final_data = AC_func(method_lst, input_data, data_len)
    
    if type(final_data) != str:
        final_data = '[' + ','.join(map(str, final_data)) + ']'
    
    print(final_data)