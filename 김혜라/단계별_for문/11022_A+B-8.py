import sys
N = int(sys.stdin.readline().rstrip())

for i in range(1, N+1):
    print(f'Case #{i}: ', end="")
    A , B = map(int, sys.stdin.readline().rstrip().split())
    print(A, "+", B, "=", A+B)