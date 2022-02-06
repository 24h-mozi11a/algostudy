x, y, w, h = map(int, input().split(' '))
if w - x <= w//2:
    x = w - x
if h - y <= h//2:
    y = h - y

res = x if x < y else y
print(res)
