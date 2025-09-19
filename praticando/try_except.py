
while True:

    # try:
    #     numero = int(input('Digite um numero inteiro: '))
    #     print(f'O  dobro de {numero} é {numero *2}')
    #     break # caso o usuario digite o numero certo(numeros inteiros, o programa finaliza)
    # except ValueError:
    #     print('valor digitado  nao é um numero inteiro')

    try:
        numero = int(input('Digite um numero inteiro: '))
    except:
        print('valor invalido tente novamente')
        continue # caso o usuario digite um numero nao inteiro, esse continue volta para o loop
        #, caso o usuario digite um numero inteiro correto, ele passa para o print, avança e encerra o loop

    print(f'O dobro do {numero} é {numero * 2}')
    break



print('----------  Programa finalizado  -------------')