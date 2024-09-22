ans = ''

def palindrome(a):
    global ans #https://velog.io/@juju08217/python-UnboundLocalError-local-variable-var-referenced-before-assignment
    origin_data = a
    origin_lst = list(str(origin_data))
    
    related_lst = list()
    
    for i in range(len(origin_lst) - 1, -1, -1):
        related_lst.append(origin_lst[i])
    
    if(origin_lst == related_lst):
        ans += 'yes\n'
    else:
        ans += 'no\n'


while True:
    data = int(input())
    if(data == 0):
        break
    else:
        palindrome(data)

print(ans)