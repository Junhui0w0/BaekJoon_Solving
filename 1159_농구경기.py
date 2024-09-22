# data = str(input())
# out = list(data)
# print(out)

#97 ~ 122 => a~z 아스키코드 값
# print("%c" % 97) -> a
alpha_lst = list() #abcde . . . 저장LIST
for i in range(97,123,1):
    alpha_lst.append(chr(i))

num = int(input()) #선수 인원
name_lst = list()

for i in range(num):
    name = str(input()) #선수 이름
    data = list(name) #선수 이름의 첫번째 문자(1개)
    name_lst.append(data[0]) #선수 이름 첫 문자 저장

first_name_lst = list() #똑같은 성의 개수 저장 LIST

for i in range(97,123,1): #아스키코드 a ~ z
    relate_data = chr(i) #알파벳 a ~ z
    total = 0
    for j in name_lst:
        if(relate_data == j):
            total += 1
        else:
            continue
    first_name_lst.append(total)

printer_lst = list() #출력할 성 저장LIST
for i in range(len(first_name_lst)):
    if(first_name_lst[i] >= 5):
        printer_lst.append(alpha_lst[i])
    else:
        continue

if(len(printer_lst) == 0):
    print("PREDAJA")
else:
    for i in printer_lst:
        print(i,end="")