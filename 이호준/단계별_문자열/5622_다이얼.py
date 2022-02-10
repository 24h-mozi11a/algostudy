a = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
call = list(input())
sum = 0
for i in call:
    for j in range(len(a)):
        if i in a[j]:
            sum += j+3
print(sum)
