from pyparsing import alphanums


S = input()
result = []
# a~z 리스트 생성:
alp_list = list(map(chr, range(97, 123)))

# 알파벳을 순서대로 검증기에 넣음
for alp in alp_list:
    index = 0
    # index를 더해가면서 들어온 알파벳이 몇번 쨰 존재하는지 검증
    # 존재하면 break, 끝까지 존재 안하면 index는 len(S)와 같음
    # 그럴경우만 존재하지 않는다는 의미로 -1을 append
    for comp in S:
        if alp == comp:
            result.append(index)
            break
        else:
            index +=1
    if index == len(S):
        result.append(-1)
           
for i in result:
    print(i, end = ' ')

# 좀 오래걸림
# 함수 구조 그리면서 설명하듯이 해보니까 풀림