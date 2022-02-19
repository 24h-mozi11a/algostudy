import sys
sys.stdin = open('직사각형.txt')

paper = [[0 for _ in range(100)] for _ in range(100)]
# print(paper)

r1_x1, r1_y1, r1_x2, r1_y2 = map(int, input().split())
r2_x1, r2_y1, r2_x2, r2_y2 = map(int, input().split())
r3_x1, r3_y1, r3_x2, r3_y2 = map(int, input().split())
r4_x1, r4_y1, r4_x2, r4_y2 = map(int, input().split())

# print(r2_x1, r2_y1, r2_x2)

for i in range(r1_x1, r1_x2):
    for j in range(r1_y1, r1_y2):
        if paper[i][j] == 0:
            paper[i][j] += 1

for i in range(r2_x1, r2_x2):
    for j in range(r2_y1, r2_y2):
        if paper[i][j] == 0:
            paper[i][j] += 1

for i in range(r3_x1, r3_x2):
    for j in range(r3_y1, r3_y2):
        if paper[i][j] == 0:
            paper[i][j] += 1

for i in range(r4_x1, r4_x2):
    for j in range(r4_y1, r4_y2):
        if paper[i][j] == 0:
            paper[i][j] += 1

sum = 0
for i in range(100):
    for j in range(100):
        sum += paper[i][j]

print(sum)