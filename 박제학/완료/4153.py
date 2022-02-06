line = []
while 1:
    line = list(map(int, input().split(' ')))
    if sum(line) == 0:
        break
    line = [i**2 for i in line]
    tot = sum(line)
    res = ''
    for num in line:
        if num*2 == tot:
            res = 'right'
            break
        res = 'wrong'
    print(res)