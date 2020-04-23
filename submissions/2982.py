asd = 0
for i in range(int(input())):
    s = input().split()
    if s[0] == 'G':
        asd += -int(s[1])
    else:
        asd += int(s[1])
if asd >= 0:
    print("A greve vai parar.")
else:
    print("NAO VAI TER CORTE, VAI TER LUTA!")