n = int(input())
game = ['tesoura','pedra','Spock','papel','lagarto']
res = ['De novo!', 'Raj trapaceou!', 'Bazinga!']
i = 1
while(n > 0):
    n -= 1
    winner = 0
    s, r = input().split()
    while(game[2] != s):
            game = [game[-1]] + game[:-1]
    s = 2-game.index(r)
    if(s > 0):
        winner = 2 #shel
    elif(s < 0):
        winner = 1 #raj
    else:
        winner = 0 #emp
    
    print('Caso #%d: %s' % (i, res[winner]))
    i += 1