data_lst = list(map(int,input().split()))
num = 1
count = 0

while True:
    count = 0
    if(num % data_lst[0] == 0):
        count += 1
    if(num % data_lst[1] == 0):
        count += 1
    if(num % data_lst[2] == 0):
        count += 1
    if(num % data_lst[3] == 0):
        count += 1
    if(num % data_lst[4] == 0):
        count += 1
    
    if(count >= 3):
        break
    else:
        num += 1

print(num)