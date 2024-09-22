from sys import stdin

N = int(stdin.readline())
lst = set()

for i in range(N):
    people, commute = stdin.readline().split()
    if(commute == 'enter'):
        lst.add(people)
    else:
        lst.discard(people)
        
lst2 = list(lst)
lst2.sort(reverse=True)

print(*lst2)