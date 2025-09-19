

lista = []
while True:
    print('Selecione uma opçao')
    usuario = input('[i]nserir  [a]pagar [l]istar ')
    try:
        if usuario == 'i':
             opcao = input('valor: ')
             lista.append(opcao)


        elif "a" in usuario:
            print('Nao foi possivel apagar este indice')
            continue


        elif usuario == 'l':
            if len(lista) == 0:
                print('Nada para listar')
            for i,opcao in enumerate(lista):
                print(i,opcao)

        else:
            print('Digite uma opçao válida')

    except:
        ...