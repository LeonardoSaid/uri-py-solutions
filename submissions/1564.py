while True:
    try:
      s = int(input())
      if s == 0:
        print("vai ter copa!")
      else:
        print("vai ter duas!")
      
    except EOFError:
        break