import random

print("--------------🎯 Jogo da Adivinhação--------------\n")
print("Você tem 5 tentativas para acertar um número entre 0 e 10.\n")

numero_secreto = random.randint(0,10)
#print(numero_secreto)
tentativas = 0
limite = 5

while tentativas < limite:
    try:
        entradas = int(input('Adivinha um numero de (0 até 10): '))

        if entradas < 0 or entradas > 10:
            print('Digite um Número de 0 até 10\n')
            continue

        tentativas += 1
        print(f"Tentativa {tentativas} de {limite}") # conta as tentativas pro usuário, 1 de 5 por exemplo 

        
          
        if entradas == numero_secreto:
            print(f'Parabens, voce acertou o número secreto!!! {numero_secreto}\n')
            break

        elif entradas < numero_secreto:
            print('Numero Secreto é maior')

        else:
            print('Número secreto é menor')
        # else:
        #     print('Errou! Tente novamente')

    except ValueError:
        print('Digite apenas números inteiros!\n')

    except Exception as e:
        print(f'Erro No Sistema {e}')

if tentativas == limite and entradas != numero_secreto:
    print(f'Suas tentativas acabaram!\n Numero secreto era {numero_secreto}')