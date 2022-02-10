N = int(input())
result = 0
while True:
    if N % 5 == 0:
        print(N // 5)
        break
    if N == 0:
        print(result)
        break    
    N = N-3
    result += 1
    if N < 0:
        print(-1)
        break
    if N % 5 > 0:
        continue
    else:
        result += N // 5
        print(result)
        break