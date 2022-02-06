a = int(input())
f = a
n = 0
while True:
    if a >= 10:
        b = a // 10
        c = a % 10
        a = (b + c) % 10 + c * 10
        n += 1
        if a == f:
            print(n)
            break
    if a < 10:
        a = a * 10 + a
        n += 1
        if a == f:
            print(n)
            break
