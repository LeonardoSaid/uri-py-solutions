k = int(input())

while k > 0:

  s = input()

  if s[0] == s[2]:
    print(int(s[0]) * int(s[2]))
  elif ord(s[1]) >= 65 and ord(s[1]) <= 90:
    print(int(s[2]) - int(s[0]))
  else:
    print(int(s[0]) + int(s[2]))

  k -= 1