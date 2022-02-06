x = int(input())
y = int(input())

if x > 0 and y > 0:
    a = 1

elif x > 0 and y < 0:
    a = 4

elif x < 0 and y > 0:
    a = 2

else:
    a = 3

print(a)
print(f'{a}사분면에 속합니다')