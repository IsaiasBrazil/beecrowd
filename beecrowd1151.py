n=int(input())
def fib(n):
    if n <= 1:
        return n
    return fib(fib(n-1)+fib(n-2))
print(fib(n))
