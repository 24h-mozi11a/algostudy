M = int(input())
N = int(input())
total = 0
min = 0
for i in range(N, M-1, -1):
    if i == 1:
        continue
    res = 0
    for n in range(2, i):
        if i % n == 0:
            res += 1
    if res == 0:
        total += i
        min = i
if total == 0:
    print(-1)
else:
    print(total)
    print(min)