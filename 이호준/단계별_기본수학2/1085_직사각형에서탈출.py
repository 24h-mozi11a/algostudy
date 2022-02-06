x, y, w, h = map(int, input().split())
a = w - x
b = h - y
list1 = [a, b, x, y]
list1.sort()
print(list1[0])