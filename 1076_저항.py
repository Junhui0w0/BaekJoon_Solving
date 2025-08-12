from collections import deque
import sys
input = sys.stdin.readline

#입력
    #1. Color_1: 1번 색깔 입력
    #2. Color_2: 2번 색깔 입력
    #3. Color_3: 3번 색깔 입력

#실행 및 출력
    #1. 첫번째와 두번째 입력된 색깔의 값은 서로 연결한다.
    #2. 이후 연결된 값을 세번째 입력된 색깔의 저항을 곱한다.

data_lst = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
length = len(data_lst)

color1 = str(input().rstrip())
color2 = str(input().rstrip())
color3 = str(input().rstrip())

color1_index = data_lst.index(color1)
color2_index = data_lst.index(color2)
color3_index = data_lst.index(color3)

ans = 10 * color1_index + color2_index
ans = ans * (10**color3_index)

print(ans)