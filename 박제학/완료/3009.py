x = []
y = []
for i in range(3):
    x_dot, y_dot = map(int, input().split(' '))
    x.append(x_dot)
    y.append(y_dot)

x_res = 0
y_res = 0

for i in x:
    if x.count(i) == 1:
        x_res = i

for j in y:
    if y.count(j) == 1:
        y_res = j

print(f'{x_res} {y_res}')
