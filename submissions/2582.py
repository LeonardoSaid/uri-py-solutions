a = ['PROXYCITY', 'P.Y.N.G.', 'DNSUEY!', 'SERVERS', 'HOST!', 'CRIPTONIZE', 'OFFLINE DAY', 'SALT', 'ANSWER!', 'RAR?', 'WIFI ANTENNAS']

n = int(input())

while n > 0:
    
    x,y = map(int, input().split())

    print(a[x+y])

    n -= 1