# nota1 = float(input('Digite sua primeira nota: '))
# nota2 = float(input('Digite sua segunda nota: '))
# nota3 = float(input('Digite sua terceira nota: '))

# media = (nota1+nota2+nota3)/3

# if media >= 7:
#     print(f'parabens, voce foi aprovado, sua media foi {media:.2f}')

# elif media >=4 and media <7:
#     print(f'voce esta de recuperaçao, sua media foi {media:.2f}')

# else:
#     print(f'voce esta reprovado! sua media foi {media:.2f}')

# Calculadora
# try:

#     numero1 = float(input('Digite um numero: '))
#     numero2 = float(input('Digite um numero: '))
#     operacao =  input('Qual operaçao voce deseja efetur? + , - , / , * : ')


    
#     if '+' in operacao:
#         print(f'A soma de {numero1} + {numero2} = {numero1 + numero2}')

#     elif '-' in operacao:
#         print(f'A subtracao  de {numero1} - {numero2} = {numero1 - numero2}')

#     elif '/' in operacao:
#         print(f'A divisao de {numero1} / {numero2} = {numero1 / numero2}')

#     elif '*' in operacao:
#         print(f'A multiplicacao de {numero1} * {numero2} = {numero1 * numero2}')

#     else:
#         print('Digite um numero valido')

# except ZeroDivisionError:
#     if numero2 == 0:
#         print('Nao é possivil fazer divisoes por 0')

# usuario = input('Digite seu nome: ')
# usuario_invertido = usuario[::-1]


# for i in usuario_invertido:
#     print(f'Seu nome ivertido é {i}')

# for i in range(1,10):
#     print(i)

# numero_tabuada = int(input('Digite um Número para tabuada: '))

# for indice in range(1,11):
#     print(f'A tabuada  {numero_tabuada} X {indice} = {numero_tabuada*indice}')

# soma = 0
# for i in range(5):
#     numeros = int(input(f'Digite {i+1} numero: '))
#     soma = soma + numeros
    
# print(f'Resultado das somas é {soma}')

# contador = 0

# while(contador <10):
#     contador +=1

#     print(contador)

# digite_numero = int(input('Digite um numero: '))

# while(digite_numero > 0):
#     digite_numero -=1
#     print(digite_numero)


# senha = 123456

# try:

#     while True:
#         digite_senha = int(input('Digite uma senha: '))

#         if digite_senha == senha:
#             print('Acesso Liberado!')
#             break
        
#         else:
#             print('Senha Incorreta! Tente novamente')

# except Exception as e:
#     print(f'Digite um numero valido -> {e}')

# while True:
#     print('1- Dizer Olá!')
#     print('2- Dizer Tchau!')
#     print('3- Sair do sistema')

#     digite = input('Digite uma opcao acima: ')

#     if digite == '1':
#         print('Olá, seja Bem-Vindo!')
#         print('---------NUBANK----------')
#         print('----------------------------------------')

#     if digite == '2':
#         print('Tchau! Até a próxima...')
        
    
#     if digite == '3':
#         print('Voce saiu do programa! \n')
#         break
    
#     else:
#         print('Digite um numero válido! \n')

# try:
#     numero = int(input('Digite um numero Inteiro: '))
#     print(f'Numero inteiro {numero}')
 
# except:
#     print('Por favor, Digite um numero Inteiro')

# try:

#     numero1 = int(input('Digite um Numero: '))
#     numero2 = int(input('Digite outro numero: '))


#     if numero2 == 0:
#         print(f'Nao é possivel divisão por 0')

#     else:
#         res = numero1 / numero2
#         print(f' O resultado da sua divisao é {res}')

# except ZeroDivisionError:
#     print('Nao é possivel Divisao por 0')

# except ValueError:
#     print(f'Digite um numero Valido')

# except Exception as e:
#     print(f'Ocorreu um erro inesperado! {e}')

# while True:  
#     try:
#         entrada = input('Digite sua idade: ')
#         idade = int(entrada)
#         print(f'Voce têm {idade} anos')
#         break

#     except ValueError:
#         print(f'Digite uma idade valida "{entrada}", Digite novamente.')

# numeros = []

# while True:
#     try:
#        entrada = int(input(f'Digite o {len(numeros)+1} numeros: '))
#        numeros.append(entrada)
           
#     except ValueError:
#         print('Digite algo valido')
        

#     if len(numeros) == 5:
#         break
# soma = sum(numeros)

# print(f'Numeros digitados foram {numeros}')
# print(f'A soma dos numeros digitados foram {soma}')

