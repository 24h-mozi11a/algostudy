def self_n(n):
    res = 0
    while n != 0:
        res += n%10
        n = n//10
    return res

n = 10001
test_set = [i for i in range(1, n)]
for num in test_set:
    if type(num) == int:
        while num<n:
            num = num + self_n(num)
            if num < n:
                test_set[num-1] = ''

for res in test_set:
    if type(res) == int:
        print(res)

# 좀 길어짐, ****인덱스 번호 0부터 시작하는거 주의!!!****
# *** 무한루프 걸릴 때 돌아가는 변수 출력해서 왜그런지 보기***
