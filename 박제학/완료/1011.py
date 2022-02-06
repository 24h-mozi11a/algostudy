T = int(input())
for i in range(T):
    x, y = map(int, input().split(' '))
    length = y-x
    count = 0
    while length > 2*(count+1):
        count += 1
        length -= count*2
    if 2*(count + 1) >= length > count+1:
        print(2*(count+1))
    elif count+1 >= length > 0:
        print(2*count + 1)
    else:
        print(2*count)