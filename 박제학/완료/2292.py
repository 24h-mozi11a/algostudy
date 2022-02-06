N = int(input())
an = 1
d = 6
i = 1
while N > an:
    an += d*i
    i += 1

print(i)

# 철저하게 수학적으로 접근하는게 오히려 쉬움