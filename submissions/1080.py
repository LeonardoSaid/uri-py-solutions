d = list()
for i in range(100):
  d.append(int(input()))
print(max(d))
print(d.index(max(d))+1)