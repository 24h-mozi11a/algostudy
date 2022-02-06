# list로 변환 후 아스키코드 처리하고 A아스키코드 값 빼서 
# //3 했을 때 값 따라 숫자 부여할 예정
word = input()
word = list(word)
# 한 숫자에 4개 들어가는것들 처리
for i in range(len(word)):
    if word[i] == 'S':
        word[i] = 'R'
    if word[i] == 'V':
        word[i] = 'U'
    if word[i] == 'Y' or word[i] == 'Z':
        word[i] = 'X'
word = list(map(ord, word))
word = list(map(lambda x : (x-65)//3, word))

for i in range(len(word)):
    word[i] += 3
result = 0
for n in word:
    result += n
print(result)

#문제 조건 제대로 안읽어서 오래걸림
# 조건 제대로 읽기!!!