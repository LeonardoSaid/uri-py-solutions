def printapar(a):
    for i in range(0, len(a)):
        print("par[%d] = %d" % (i, a[i]))
        
def printaimpar(a):
    for i in range(0, len(a)):
        print("impar[%d] = %d" % (i, a[i]))

par = list()
impar = list()

for i in range(15):
    x = int(input())
    
    if x % 2 == 1:
        if len(impar) == 5:
            printaimpar(impar)
            impar = list()
        impar.append(x)
    else:
        if len(par) == 5:
            printapar(par)
            par = list()
        par.append(x)

printaimpar(impar)
printapar(par)