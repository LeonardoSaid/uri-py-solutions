while True:
    n = int(input())
    if n == 0:
        break

    c = n * n
    res = ""
    s = 'ABCD'

    res = s[c % 4] + res
    c = c // 4

    while c != 0:
        res = s[c % 4] + res
        c = c // 4

    print(res)

