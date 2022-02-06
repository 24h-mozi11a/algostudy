T = int(input())
for repit in range(T):
    result = ''
    R, S = input().split(' ')
    R = int(R)
    for char in S:
        result += char*R
    print(result)

# input().split('')로 여러개 따로 받아짐