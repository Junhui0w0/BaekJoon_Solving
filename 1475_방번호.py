from sys import stdin
n = stdin.readline()

n_lst = list(n)
lst = list()

for i in range(10):
    lst.append(n_lst.count(str(i))) #0~9 갯수를 차례대로 lst에 저장
six_and_nine = lst[6] + lst[9]
total = int((six_and_nine) / 2) + (six_and_nine % 2)

lst[6] = 0
lst[9] = total

print(max(lst))