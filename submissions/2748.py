nome = 'Roberto'
num = '5786'
uni = 'UNIFEI'

traco = ''.join('-' for i in range(39))
linhanome = '|'+''.join(' ' for i in range(8))+nome+''.join(' ' for i in range(29-len(nome)))+'|'
linhanum = '|'+''.join(' ' for i in range(8))+num+''.join(' ' for i in range(29-len(num)))+'|'
linhauni = '|'+''.join(' ' for i in range(8))+uni+''.join(' ' for i in range(29-len(uni)))+'|'

linhab = '|'+''.join(' ' for i in range(37))+'|'




print(traco)
print(linhanome)
print(linhab)
print(linhanum)
print(linhab)
print(linhauni)
print(traco)