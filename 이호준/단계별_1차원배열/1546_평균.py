N = int(input())
scores = list(map(int, input().split()))
for i in range(len(scores)-1, 0, -1):
    for j in range(i):
        if scores[j] > scores[j+1]:
            scores[j], scores[j+1] = scores[j+1], scores[j]
S = 0
for i in scores:
    S += i
avg = (S / scores[-1] * 100) / len(scores)
print(avg)