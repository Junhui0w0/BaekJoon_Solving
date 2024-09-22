N = int(input())

coord = [list(map(int, input().split())) for i in range(N)]
#print(coord) #디버깅
coord.sort()

#print(f'\n\n\n\n{coord}')

for i in range(N):
    print(*coord[i])


#List안에 (~,~) 있을 때, sort를 사용하면 첫번째 값 sort 후 두번째 값 sort 진행함