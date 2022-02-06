from posixpath import split


A, B, C = map(int, input().split(' '))
benefit = C - B
if benefit <= 0:
    print(-1)
else:
    cross = A//benefit + 1
    print(cross)
