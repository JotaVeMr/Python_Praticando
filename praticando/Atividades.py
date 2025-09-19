# Escreva um programa que mostre os números de 1 a 10 usando for. ok
# Peça ao usuário um número e mostre a tabuada dele de 1 a 10.
# Calcule a soma de todos os números de 1 a 100.
# Peça ao usuário para digitar 5 nomes e depois mostre-os um por um.
# Mostre apenas os números pares de 1 a 20.
# Mostre os números de 10 até 1 em ordem decrescente.
# Dada a lista ["maçã", "banana", "laranja", "uva"], mostre cada fruta da lista.
# Peça ao usuário um número e conte quantos números de 1 até esse número são múltiplos de 3.
# Crie um programa que mostre a palavra "Python" 10 vezes.
# Escreva um programa que mostre todos os caracteres de uma palavra digitada pelo usuário, um por linha.
  
# tabuada = int(input('Digite um número: '))

# for i in range(1,11):
#     res =  tabuada * i
#     print(f'{tabuada} x {i} = {res}')

# soma = 0
# for i in range(1,101):
#     soma += i
    
#     print(f'soma dos resultados é {soma}')    
# nomes = []

# for i in range(5):
#     nome = input(f"Digite o nome {i+1}: ")
#     nomes.append(nome)

# # Mostrar os nomes digitados um por um
# print("\nOs nomes digitados foram:")
# for nome in nomes:
#     print(nome)

# for i in range(0,21):
#     if i % 2 == 0:
#         print(i)

# for i in range(10,1, -1):
#     print(i)

# frutas = ['Maça','Uva','Banana','Melancia']

# for i in frutas:
#     print(f'Frutas selecionadas {i}')

 
for i in range(10):
    if i ==2:
        continue
    
    if i == 6:
        continue

    if i == 9:
        print(f'quando o laco passa pelo i -> {i}, ele finaliza')
        break

    print(i)