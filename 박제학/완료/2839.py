N = int(input())
count = 0
while N % 5 != 0:
    N -= 3
    if N < 0:
        print(-1)
        break
    count += 1
count += N // 5
if N % 5 == 0:
    print(count)