num = int(input())
lst = list() #문자 넣을 list
count_lst = list() #문자열 길이 list

len_sorted_list = list() #문자를 정렬시켜 새로 넣을 list
sorted_list = list()


for i in range(num):
    string = str(input())

    lst.append(string)
    count_lst.append(len(string))

#print('\n',lst)
#print('\n',count_lst,'\n')

n = num
while (n != 0):   #길이순 정렬
    min_data = min(count_lst) #문자열 길이 최소값
    min_index = count_lst.index(min_data) #그 최소값의 index(위치)

    len_sorted_list.append(lst[min_index])
    count_lst[min_index] = 100

    n = n - 1
#print(len_sorted_list)

count_lst = list() #다시 초기화
for i in range(num):
    count_lst.append(len(len_sorted_list[i]))
#print(count_lst)


#문자 개수 작은대로 정렬은 끝남
    #아래부터 사전순 작은 것 정렬 코드짜기

    #카운트 리스트의 최소값 -> 100
    #문자열도 z보다 큰 값으로 설정
    #z보다 큰 문자열 = '{'

for i in range(num-1):
    temp_lst = list() #문자열 길이가 같은 것끼리 저장시킬 list
    counter = 0 #최소값 counter
    min_len_data = min(count_lst) #문자열 길이의 최소값
    
    for ii in range(num):
        if(min_len_data == count_lst[ii]):
            temp_lst.append(len_sorted_list[ii])
            count_lst[ii] = 100
            #len_sorted_list[ii] = chr(123)
            counter += 1
    
    if(counter == 1):
        sorted_list.append(temp_lst[0])
    elif(counter >= 2):
        temp_lst.sort()
        for v in range(len(temp_lst)):
            sorted_list.append(temp_lst[v])
    
    print(sorted_list[i])
    #print('\n','TEMP LIST : ',temp_lst,'\n')

