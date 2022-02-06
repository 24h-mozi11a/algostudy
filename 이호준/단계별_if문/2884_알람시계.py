a, b = map(int, input().split())
minute = a * 60 + b
result = minute - 45
if result > 1440:
    result -= 1440
elif result < 0:
    result += 1440
a = result // 60
b = result % 60
print(a, b)