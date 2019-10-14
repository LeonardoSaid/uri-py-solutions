# https://stackoverflow.com/questions/2489435/check-if-a-number-is-a-perfect-square
def is_square(apositiveint):
    if apositiveint == 1:
        return True
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True


for i in range(int(input())):
    n = int(input())
    han = [0 for k in range(n)]
    c = 0
    num = 1
    while True:

        if c >= n:
            break

        if is_square(num + han[c]) or han[c] == 0:
            han[c] = num
            num += 1
            c = 0
        else:
            c += 1
    print(num - 1)