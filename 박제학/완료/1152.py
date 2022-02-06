s = input()
pad = [' ']
s = list(s) + pad
count = 0
for i in range(len(s)-1):
    if s[i] != ' ' and s[i+1] == ' ':
        count += 1
print(count)
# 문자+공백이면 카운트 하는 건 생각했는데
# 패딩해주는걸 생각하는데 오래걸림