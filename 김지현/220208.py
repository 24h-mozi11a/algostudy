## 1110

# num = 26 #int(input())
# cycle = 0
# new_num = 0

# while new_num!= num:
    
#     if num < 10:
#         new_num = 11 * num
#         cycle += 1
#         new_num = new_num // 10 + new_num % 10
#         cycle += 1
#     else:
#         # 10보다 큰 경우, 각자리 수의 숫자를 더하고
#         # 10으로 나눈 몫(십의 자리 수)과 10으로 나눈 나머지(일의 자리 수)
#         new_num = num // 10 + num % 10
#         new_num = num 
#         if new_num > 10:
#             # 10을 넘기면 다시 일의 자리 수만
#             new_num = new_num % 10


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