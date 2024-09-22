num = int(input())
lst = list()
str_len = 0
tmp = 0 #첫번쨰 리스트 index

for i in range(num):
    str_data = str(input())
    lst.append(list(str_data))
    str_len = len(str_data)

for