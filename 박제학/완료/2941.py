s = input()
s = list(s) + [' ']
# 크로아티아 알파벳 리스트 생성
cra_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
for i in range(len(s)-2):
    if s[i] + s[i+1] + s[i+2] in cra_list:
        count += 1
        s[i], s[i+1], s[i+2] = ' ', ' ', ' '
    if s[i] + s[i+1] in cra_list:
        count += 1
        s[i], s[i+1] = ' ', ' '

for i in range(len(s)):
    if s[i] != ' ':
        count += 1
print(count)

# 좀 지저분한데 금방함
# 더 줄일수 있을지 생각해봐야될듯