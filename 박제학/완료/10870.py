N = int(input())
def fib(x):
    if x <=1:
        return x
    return fib(x-1)+fib(x-2)
print(fib(N))