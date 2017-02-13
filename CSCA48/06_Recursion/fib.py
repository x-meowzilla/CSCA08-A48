def fib(n):
    if (n < 2):
        result = 1
    else:
        a = fib(n - 1)
        b = fib(n - 2)
        result = a + b
    return result


if (__name__ == "__main__"):
    print(fib(5))
