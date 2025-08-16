from collections import deque
import sys
input = sys.stdin.readline

sudoku_lst = []
zero_pos_lst = []

row_lst = [([False] * 10) for _ in range(9)] #row_lst[x][y] -> x: 행의 위치 (0,1,...8행) / y: 해당 행에 index 값이 있는가? -> ex) [1][3] -> 1행에 3이 있다.
col_lst = [([False] * 10) for _ in range(9)] #col_lst[x][y] -> x: 열의 위치(0,...8열) / y: 해당 열에 index 값이 있는가? -> ex) [1][3] -> 1열에 3이 있다.
region_lst = [([False] * 10) for _ in range(9)]
    #1. 스도쿠 판(9x9)을 3x3 형태로 총 9칸으로 나눈다.
    #2. 이때, 좌상단에 위치한 3x3 형태의 값은 region_lst[0]에 저장하고, 우하단에 위치한 3x3 형태의 값들은 region_lst[8]에 저장한다.
    #3. 그럼 아래와 같은 식이 성립한다.
        #- region_lst[(i//3) * 3 + (j//3)][y] -> (i//3) * 3 + (j//3) 구역에 y값이 있다.

for i in range(9):
    input_data = list(map(int, input().rstrip().split()))
    sudoku_lst.append(input_data)

    for j in range(9):
        if input_data[j] == 0: #빈칸 위치
            zero_pos_lst.append((i, j))

        else: #빈칸이 아님
            region_num = (i//3) * 3 + (j//3)
            row_lst[i][input_data[j]] = True 
            col_lst[j][input_data[j]] = True
            region_lst[region_num][input_data[j]] = True

def get_answer(cur_idx):
    if cur_idx == len(zero_pos_lst): #빈칸이 채워진 경우
        for data in sudoku_lst:
            print(*data)    
        return 'Get Sudoku'

    x, y = zero_pos_lst[cur_idx][0], zero_pos_lst[cur_idx][1] #빈칸이 있는 위치 - x=행/ y=열
    region_idx = (x//3) * 3 + (y//3) #- 빈칸이 위치한 3x3 구역

    for value in range(1, 9+1):
        if not row_lst[x][value] and not col_lst[y][value] and not region_lst[region_idx][value]:
                #- ex) 2행에 3값이 True (즉, 2행에 3이 있다.) 라고 하면 not row_lst[x][value] == False이기에 위 조건식은 성립X -> 다음 value갑 삽입
            row_lst[x][value] = True
            col_lst[y][value] = True
            region_lst[region_idx][value] = True
            sudoku_lst[x][y] = value

            tmp = get_answer(cur_idx+1)

            if tmp == 'Get Sudoku':
                return tmp

            row_lst[x][value] = False
            col_lst[y][value] = False
            region_lst[region_idx][value] = False
            sudoku_lst[x][y] = 0

get_answer(0)