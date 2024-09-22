n = int(input()) #약수의 개수

data_lst = list(map(int,input().split())) #약수 입력
min_data = min(data_lst)
max_data = max(data_lst)

print(max_data * min_data)