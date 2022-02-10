T = int(input())
for tc in range(1, T+1):
    k = int(input())
    n = int(input())
    f = list(range(1,15))

    for _ in range(k):
        f_2 = []
        for i in range(14):
            a = 0
            for j in range(i+1):
                a += f[j]
            f_2 += [a]
        f = f_2
    print(f[n-1])