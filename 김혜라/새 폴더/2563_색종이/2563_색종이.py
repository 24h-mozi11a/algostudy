import sys; sys.stdin = open('2563_색종이.txt')

paper = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())
for _ in range(n):
    x1, y1 = map(int,input().split())

    for i in range(x1, x1 + 10):
        for j in range(y1, y1 + 10):
            if paper[i][j] == 0:
                paper[i][j] += 1

    sum = 0
    for i in range(100):
        for j in range(100):
            sum += paper[i][j]
print(sum)

