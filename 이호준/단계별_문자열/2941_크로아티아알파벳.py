a = input()
cro = ['c=', 'c-', 'dz=', 'd=', 'lj', 'nj', 's=', 'z=']
cnt = 0
for word in cro:
    if word in a:
        if a.count(word) >= 2:
            cnt += a.count(word) - 1
        cnt += 1
        a = a.replace(word, ' ')
a = a.replace(' ', '')
cnt += len(a)
print(cnt)