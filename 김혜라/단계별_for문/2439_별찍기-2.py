import sys
N = int(sys.stdin.readline().rstrip())

for i in range(0, N + 1):
    print(i*'*'.rjust(N))