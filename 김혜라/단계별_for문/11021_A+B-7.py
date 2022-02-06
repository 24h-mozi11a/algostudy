import sys

T = int(sys.stdin.readline().rstrip())
for i in range(1,T+1):
    print(f'Case #{i}: ', end="")
    a , b = map(int, sys.stdin.readline().rstrip().split())
    print(a + b)