S = input()
S = S.upper()
# 알파벳별 값 dict로 못만들겠어서 각자 따로 저장하고 index로 쓸 예정 
alp = ''
num = []
# set형태로 바꿔서 중복제거
set_S = set(S)
for element in set_S:
    count = 0
    # 입력받은 문자열 순회해서 횟수 카운트
    for comp in S:
        if element == comp:
            count += 1
    alp += element
    num.append(count)
max_num = 0
max_alp = ''
for i, n in enumerate(num):
    n = int(n)
    if n > max_num:
        max_num = n
        max_alp = alp[i]
    elif n == max_num:
        max_alp = '?'

print(max_alp)

# max_alp 를 max_apl로 써서 20분 헤맴ㅋㅋ