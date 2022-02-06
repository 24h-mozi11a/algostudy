T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    first = [i for i in range(1, n + 1)]
    second = first[::1]
    # k층번 반복
    for b in range(k):
        # first의 값을 전층의 합으로 할당
        first = second[::1]
        # 리스트의 인덱스
        for j in range(1, n):
            temp = 0
            for a in range(j+1):
                temp += first[a]
            second[j] = temp
    print(second[-1])

    # 리스트 끼리 할당하면 원본이 바뀌는걸 까먹어서 오래 해멤.
    # 얕은복사, 깊은복사 잘 생각하기!