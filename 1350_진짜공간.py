file_num = int(input()) #파일 개수
file_lst = list(map(int,input().split())) #파일 크기
clu_size = int(input()) #클러스터 크기

total = 0
for data in file_lst:
    if(data == 0):
        continue
    else:
        if(data % clu_size == 0): #나누어 떨어지는 경우
            total += (data // clu_size) * clu_size
        else: #나머지가 있는 경우
            total += (data // clu_size + 1) * clu_size

print(total)