X = int(input())
an = 0 # 첫항
i = 1 # 1씩 더해가며 더할 변수
while 1:
    an = an + i
    if an >= X:
        an = an - i
        break
    i += 1
tot = i + 1  # 분자 분모 총 합
n = X - an 
top = n
bot = tot - top
if tot % 2 == 0:
    top, bot = bot, top 
print(f'{top}/{bot}')
