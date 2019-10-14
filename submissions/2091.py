from collections import Counter

while True:
    n = int(input())
    if n == 0:
        break
    c = list(map(int, input().split()))

    # a list could be used in the same way, but a Counter is more efficient
    for key, count in Counter(c).items():
        if count % 2:
            print(key)