from collections import deque
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

#입력
    #1. [...] (9x9크기의 스도쿠 판)

#실행
    #1. 스도쿠 판은 0~9의 정수로 구성되어 있다.
    #2. 0은 빈칸을 나타내고 있다.

#출력
    #1. 0을 적절한 숫자로 채워 스도쿠 규칙에 맞는 판을 출력한다.

sudoku_lst = []
zero_pos_lst = []
ans = []

for i in range(9):
    input_data = list(map(int, input().rstrip().split()))
    sudoku_lst.append(input_data)

    for j in range(9):
        if input_data[j] == 0: #빈칸 위치
            zero_pos_lst.append((i, j))

# print(zero_pos_lst)

def check_rule(cur_x, cur_y, value):
    # print(f'cur_x: {cur_x} / cur_y: {cur_y} / value: {value}')

    # #1. 가로 검사 -> cur_y값
    # row_set = set()
    # row_set.add(value)
    # for data in sudoku_lst[cur_x]:
    #     if data == 0:
    #         continue

    #     if data in row_set:
    #         return 'Error'
        
    #     row_set.add(data)
        
    # #2. 세로 검사 -> cur_x값
    # col_set = set()
    # col_set.add(value)
    # for i in range(9):
    #     if sudoku_lst[i][cur_y] == 0:
    #         continue

    #     if sudoku_lst[i][cur_y] in col_set:
    #         return 'Error'
        
    #     col_set.add(sudoku_lst[i][cur_y])

    # #3. 3x3 검사 -> cur_x//3 & cur_y//3 값
    # div_x = (cur_x//3) * 3
    # div_y = (cur_y//3) * 3
    # region_set = set()
    # region_set.add(value)

    # for i in range(div_x, div_x+3):
    #     for j in range(div_y, div_y+3):
    #         if sudoku_lst[i][j] == 0:
    #             continue

    #         if sudoku_lst[i][j] in region_set:
    #             return 'Error'
            
    #         region_set.add(sudoku_lst[i][j])

    #검사 결합
    row_set = set()
    col_set = set()
    row_set.add(value)
    col_set.add(value)

    div_x = (cur_x//3) * 3
    div_y = (cur_y//3) * 3
    region_set = set()
    region_set.add(value)

    for i in range(9):
        #1. 행 검사
        if sudoku_lst[cur_x][i] in row_set:
            return 'Error'

        #2. 열 검사
        if sudoku_lst[i][cur_y] in col_set:
            return 'Error'

        #3. 3x3 region 검사
        if sudoku_lst[div_x + (i//3)][div_y + (i%3)] in region_set:
            return 'Error'
        

        
        if sudoku_lst[cur_x][i] != 0:
            row_set.add(sudoku_lst[cur_x][i])

        if sudoku_lst[i][cur_y] != 0:
            col_set.add(sudoku_lst[i][cur_y])

        if sudoku_lst[div_x + (i//3)][div_y + (i%3)] != 0:
            region_set.add(sudoku_lst[div_x + (i//3)][div_y + (i%3)])

    #4. 아래 코드는 넣은 값(value)가 정답일 때 수행
    return True

def next_step(cur_idx):
    x, y = zero_pos_lst[cur_idx][0], zero_pos_lst[cur_idx][1]

    for value in range(1, 9+1):
        ret_check = check_rule(x, y, value)

        if ret_check == True: #값을 둘 수 있다면?
            sudoku_lst[x][y] = value

            if sudoku_lst[zero_pos_lst[-1][0]][zero_pos_lst[-1][1]] != 0: #스도쿠에 값을 두는 것을 종료하는 경우
                # print(zero_pos_lst[-1][0], zero_pos_lst[-1][1])
                return 'Fin'
            
            ret_next = next_step(cur_idx+1)

            if ret_next == 'Fin':
                return ret_next
            
            elif ret_next == 'End Value':
                sudoku_lst[x][y] = 0

        if value == 9:
            return 'End Value'


if len(zero_pos_lst) == 0:
    for data in sudoku_lst:
        print(*data)

elif len(zero_pos_lst) == 1:
    x, y = zero_pos_lst[0][0], zero_pos_lst[0][1]

    for value in range(1, 9+1):
        ret_check = check_rule(x,y,value)

        if ret_check == True:
            sudoku_lst[x][y] = value
            break

    for data in sudoku_lst:
        print(*data)

else:
    x, y = zero_pos_lst[0][0], zero_pos_lst[0][1]

    for value in range (1,9+1):
        # print(value)
        ret_check = check_rule(x, y, value)

        if ret_check == True: #해당 좌표에 값을 둘 수 있다면?
            sudoku_lst[x][y] = value #값을 둬
            ret_next = next_step(1)

            if ret_next == 'Fin': #스도쿠 마지막 좌표에 값을 집어 넣었다면?
                break

            sudoku_lst[x][y] = 0

    # print()
    for data in sudoku_lst:
        print(*data)
