while True:
    try:

        s = input()
        if s == 'esquerda':
            print("ingles")
        elif s == 'direita':
            print('frances')
        elif s == 'nenhuma':
            print('portugues')
        else:
            print('caiu')

    except EOFError:
        break