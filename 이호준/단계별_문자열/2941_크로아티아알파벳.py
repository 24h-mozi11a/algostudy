a = input()
cro = ['c=', 'c-', 'dz=', 'd=', 'lj', 'nj', 's=', 'z=']
cnt = 0
for alphabet in cro:
    if alphabet in a:
        if a.count(alphabet) >= 2:
            cnt += a.count(alphabet) - 1
        cnt += 1
        a = a.replace(alphabet, ' ')
a = a.replace('-', '')
a = a.replace('=', '')
a = a.replace(' ', '')
cnt += len(a)
print(cnt)