num = 1
lst = list()

for i in range(1,50):
    for ii in range(num):
        lst.append(i)
    num+=1


total =0
A,B=list(map(int,input().split()))
for i in range(A-1,B,1):
    total += lst[i]

print(total)