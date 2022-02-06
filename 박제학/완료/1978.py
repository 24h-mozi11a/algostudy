N = int(input())
numbers = list(map(int, input().split(' ')))
count = 0

for number in numbers:
    res = 0
    if number == 1:
        continue
    for n in range(2, number):
        if number % n == 0:
            res += 1
    if res == 0:
        count += 1
print(count)

# while로 나눠질때까지 돌려서 자신이면 카운트했는데 시간초과뜸
# 왜뜨는지 모르겠네
