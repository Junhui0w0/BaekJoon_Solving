from sys import stdin,stdout

n,m = map(int,stdin.readline().rstrip().split()) #n = list 개수 / m =시행 횟수
d = list(map(int, stdin.readline().split())) 
lst = [d[0]]

for i in range(1,n):
    lst.append(lst[i-1] + d[i])

#print(lst) #디버깅


for i in range(m):
    start, end = map(int, stdin.readline().rstrip().split())
    start = start - 1
    end = end -1 

    if(start == 0):
        print(str(lst[end]))
    elif(start == end):
        print(str(d[end]))
    else:
        print(str(lst[end] - lst[start-1]))