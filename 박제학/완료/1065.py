def test(n):
    n = str(n)
    gap = []
    if len(n)==1:
        return 1
    for i in range(len(n)-1):
        gap.append(int(n[i]) -int(n[i+1]))
    set_gap = set(gap)
    result = len(set_gap)
    return result

num = int(input())
result = 0
for n in range(1, num+1):
    if test(n) == 1:
        result +=1

print(result)

# 1~9케이스는 test 함수에서 처리가 안된다..
# input받고 값에 따라 더해줄지
# 함수를 다 커버 가능하게 수정할 지
# 뭐가 더 깔끔한지 모르겠다.