# fast fib using memorization (https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series)
def fib(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib(n - 1, computed) + fib(n - 2, computed)
    return computed[n]


def fib_numcalls(n):
    return 2 * fib(n + 1) - 2


for i in range(int(input())):
    x = int(input())
    print('fib(%d) = %d calls = %d' % (x, fib_numcalls(x), fib(x)))
