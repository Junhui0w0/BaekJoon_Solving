import sys
input = sys.stdin.readline

roma_lst = [('I', 1), ('V', 5), ('X', 10), ('L', 50)]
    #N = 1 -> I / V / X / L
    #N = 2 -> II-IV-IX-IL / VV-VX-VL...

# answer_set = set()
check_lst = [False] * (1001) #N <= 20 & 최대값 50 -> 50 x 20 = 1000 -> index = 0 ~ 1000
# print(check_lst)
cnt = 0

N = int(input()) #사용할 수 있는 로마 문자 갯수

def DFS(cur_length, cur_total, cur_idx):
    global cnt

    if cur_length == N:
        if check_lst[cur_total] == False:
            check_lst[cur_total] = True
            cnt += 1
        
        return True
    

    for i in range(cur_idx, 4):
        if tmp[-1] <= i:
            tmp.append(i)
            DFS(cur_length+1, cur_total + roma_lst[i][1], cur_idx)
            tmp.pop(-1)


tmp = [0]
DFS(1, 1, 0)

tmp = [1]
DFS(1, 5, 1)

tmp = [2]
DFS(1, 10, 2)

tmp = [3]
DFS(1, 50, 3)

print(cnt)