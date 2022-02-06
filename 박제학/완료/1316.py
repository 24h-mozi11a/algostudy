N = int(input())
total_count = 0 # 테스트 세트별 다 만족하면 카운트
for j in range(N):
    word = input()
    set_word = set(word)
    comp_count = 0 # 각 요소의 갯수만큼 연속되어있으면 카운트

    for comp in set_word:
        count = 0 # 각 요소의 갯수를 카운트
        for i in word: # word를 돌며 comp갯수 확인
            if i == comp:
                count += 1 

        if comp*count in word: #count 수만큼 연속된 형태가 문자열 안에 있으면 카운트
            comp_count += 1

    if comp_count == len(set_word):
        total_count += 1    

print(total_count)

# count 초기화 위치땜에 시간 엄청 날림... 중간중간 원하는대로
# 흘러가는지 프린트로 확인해보자