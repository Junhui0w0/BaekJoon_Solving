#1283_단축키 지정.py
import sys
input = sys.stdin.readline

#입력
    #1. N: 단어의 갯수
    #2. [word] (N줄): 영문 기능

#실행
    #1. 단축키 설정은 아래와 같이 할 수 있다.
        #1-1. 왼쪽에서부터 오른쪽 순서로 단어의 첫 글자가 이미 단축키로 지정되었는가를 살펴본다. 단축키가 지정이 되어있지 않다면 해당 알파벳을 단축키로 지정한다.
        #1-2. 모든 단어의 첫 글자가 이미 지정되어있다면 왼쪽에서부터 차례대로 알파벳을 단축키로 지정 안 된 것을 단축키로 지정한다.
        #1-3. 그 어떠한 알파벳도 단축키로 지정할 수 없다면 원본 상태 그대로 출력한다.
        #1-4. 이때, 대소문자는 구분하지 않는다. (즉, F와 f는 동일한 단축키로 판단한다.)

#출력
    #1. N개의 줄에 각 옵션을 출력하는데 단축키로 지정된 알파벳은 좌우에 [] 괄호를 씌워서 표현한다.

N = int(input())

word_lst = []
for _ in range(N):
    input_data = list(input().rstrip())
    word_lst.append(input_data)

danchuk_lst = set() #대소문자 구분 안함 -> upper 또는 lower 사용해서 넣어야 할듯
index_lst = []

def get_first_word(word):
    tmp = ''.join(word)
    tmp_lst = tmp.split() #띄어쓰기 기준으로 분할
    
    # print(tmp_lst)
    index = 0
    for i in range(len(tmp_lst)):
        first_word = tmp_lst[i][0]

        if first_word.upper() not in danchuk_lst: #단축키 지정 안됐으면?
            danchuk_lst.add(first_word.upper())

            if i == 0: #첫번째 단어에서 그랬으면 앞에는 어떠한 단어도 없음 == index = 0
                index_lst.append(0)

            else:
                index_lst.append(index)

            return True
        
        index += 1 + len(tmp_lst[i]) # 1=띄어쓰기 / tmp_lst[i] = 그 직전 단어 길이

    return False


for word in word_lst:
    get_danchuk = False

    ret = get_first_word(word) #띄어쓰기 기준 단축키 지정

    if ret == True:
        continue

    for index in range(len(word)):

        if word[index] == ' ': #띄어쓰기는 패스
            continue

        elif word[index].upper() not in danchuk_lst:
            index_lst.append(index) #대문자로 변경해서 넣어
            danchuk_lst.add(word[index].upper())
            get_danchuk = True
            break

    if get_danchuk == False: #단축키 설정에 실패한 경우
        index_lst.append('Not Change')

for index in range(N):
    if index_lst[index] == 'Not Change': #단축키 설정에 실패한 문자열인 경우
        print(''.join(word_lst[index])) #원본 출력

    else: #단축키 설정에 성공
        danchuk_index = index_lst[index]
        before_str = ''.join(word_lst[index][:danchuk_index])
        change_str = '['+word_lst[index][danchuk_index]+']'
        after_str = ''.join(word_lst[index][danchuk_index+1:])

        print(before_str + change_str + after_str)