s = list(map(int, input().split()))

if s[0] == s[1] or s[0] == s[2] or s[1] == s[2]:
    print('S')
elif s[0] == (s[1]+s[2]) or s[1] == (s[0]+s[2]) or s[2] == (s[1]+s[0]):
    print('S')
else:
    print('N')