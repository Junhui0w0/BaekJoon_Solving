A,B = list(map(str,input().split()))
first_lst = list(A)
second_lst = list(B)
total = 0

second_data = 0
for i in range(len(second_lst)):
    second_data += int(second_lst[i])

for i in range(len(first_lst)):
    total += second_data * int(first_lst[i])

print(total)


#시간초과 - 2중 FOR문은 절대 사용 X

# A,B = list(map(str,input().split()))
# first_lst = list(A)
# second_lst = list(B)
# total = 0

# for i in range(len(first_lst)):
#     for j in range(len(second_lst)):
#         data = int(first_lst[i]) * int(second_lst[j])
#         total += data

# print(total)