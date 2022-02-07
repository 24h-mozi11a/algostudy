## 1110

# num = int(input())
# cycle = 0
# temp = 0
# new_num = 0

# while new_num != num or (num == 0 and cycle == 0):
#     if num < 10 and cycle == 0:
#         new_num = 11 * num
#         cycle += 1
#     elif cycle == 0:
#         temp = num // 10 + num % 10
#         new_num = num % 10 * 10 + temp % 10
#         cycle += 1
#     else:
#         temp = new_num // 10 + new_num % 10
#         new_num = new_num % 10 * 10 + temp % 10
#         cycle += 1
# print(cycle)


## 2941

# a = []
# new = []
# for i in input():
#     a += i
# for n in range(0, len(a)):
#     if a[n] == 'c' and (a[n+1] == '=' or a[n+1] == '-'):
#         new += [(a[n]+a[n+1])]
#         del a[n:n+1]
#     elif a[n] == 'd' and (a[n+1] == 'z' and a[n+2] == '='):
#         new += [a[n]+a[n+1]+a[n+2]]
#         del a[n:n+2]

# print(new, a)

# a = input()
# cro_cnt = 0
# for idx in range(len(a)):
#     if a[idx] == '=':
#         if a[idx-1] in ('c', 's'):
#             cro_cnt += 1
#         elif a[idx-1] == 'z':
#             if a[idx-2] == 'd':
#                 cro_cnt += 2
#             else:
#                 cro_cnt += 1
#     elif a[idx] == '-':
#         if a[idx-1] in ('c', 'd'):
#             cro_cnt += 1
#     elif a[idx] == 'j':
#         if a[idx-1] in ('l', 'n'):
#             cro_cnt += 1
#     else:
#         cro_cnt += 0
# print(len(a) - cro_cnt)


### 1085번
# x, y, w, h = map(int, input().split())
# distance = [abs(h-y), abs(w-x), abs(x), abs(y)]
# print(min(distance))


### 3053번

from math import pi
r = int(input())

print(pi * r**2)
print(float(2 * r**2))
