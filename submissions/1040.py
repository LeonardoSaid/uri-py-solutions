n1,n2,n3,n4 = map(float, input().split())

media = ((n1*2) + (n2*3) + (n3*4) + (n4*1)) / 10

print("Media: %.1f" % media)
if(media >= 7):
    print("Aluno aprovado.")
elif(media<5):
    print("Aluno reprovado.")

if((media>=5) and (media<=6.9)):
    print("Aluno em exame.")
    ex = float(input())
    print("Nota do exame: %.1f" % ex)
    if(((ex+media)/2)>=5):
            print("Aluno aprovado.")
            print("Media final: %.1f" % ((ex+media)/2) )
    else:
            print("Aluno reprovado.")
            print("Media final: %.1f" % ((ex+media)/2) )