import math

while True:
    try:
      r = input()
      p = int(input())

      cont = 0
      contap = p

      for i in range(len(r)):

        if(r[i] == 'R'):

            if(contap == p):
              cont += 1

            if(contap == 0):
              contap = p
              cont += 1
            
            contap -= 1

        elif(r[i] == 'W'):
          cont += 1
          contap = p

      print(cont)

    except EOFError:
        break