from collections import *
#아스키코드
ascii_code = list()
for i in range(65,91,1):
    ascii_code.append(chr(i))


str_data = str(input())
str_data = str_data.upper()
c= Counter(str_data)

num_lst = list()
for i in range(26):
    num_lst.append(c[ascii_code[i]])


max_data = max(num_lst)
count = 0
for i in num_lst:
    if i == max_data:
        count += 1
    else:
        continue

if(count == 1):
    
    index = 0
    for i in num_lst:
        if(i == max_data):
            break
        else:
            index += 1

    print(ascii_code[index])

else:
    print('?')