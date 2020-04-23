while True:
    try:
      s = input()
      for i in s:
        if ((i >= 'A') and (i <= 'Z')):
            pos = ord(i)
            pos += 13;
            if (pos > 90):
                pos = (pos - 91) + 65
            print(chr(pos), end="")

        elif ((i >= 'a') and (i <= 'z')):
            pos = ord(i)
            pos += 13
            if (pos > 122):
                pos = (pos - 123) + 97
            print(chr(pos), end="")
        else:
            print(i, end="")
      print()
    except EOFError:
        break