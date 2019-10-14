insY = list()
insN = list()

while True:
    s = input().split()
    if s[0] == 'FIM':
        break

    if s[1] == 'YES' and (len(s[0]), s[0]) not in insY:
        insY.append((len(s[0]), s[0]))
    elif s[1] == 'NO' and s[0] not in insN:
        insN.append(s[0])

asd = insY[:]
insY.sort(key=lambda tup: tup[1])
insN.sort()

for i in insY:
    print(i[1])
for i in insN:
    print(i)

print()

print('Amigo do Habay:')
for i in asd:
    if i[0] == max(asd)[0]:
        print(i[1])
        break