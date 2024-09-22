#https://blog.naver.com/koreanraichu/222887840968
#안전정렬: 배열을 정렬하되 중복되는 값이 있을 땐, 입력된 순서에 맞춤
#불안전정렬:                                    무작위 순서

from sys import stdin
N = int(stdin.readline())

lst = []
for i in range(N):
    data = stdin.readline().split()
    user_data = [int(data[0]), data[1]]
    lst.append(user_data)

lst.sort(key= lambda x:x[0])

for i in lst:
    print(i[0], i[1])