import os
# Adicionando Item
# with open("meu_arquivo.txt", "a") as f:
#     f.write("Este texto será adicionado ao final.\n")
#     f.write("Outra linha adicionada.\n")
#     f.write('adicionando outra')
#     f.write('adicionando outra \n')

# Lendo Item em um arquivo
# with open("meu_arquivo.txt", "r") as f:
#     meu_conteudo = f.read()
#     print(meu_conteudo)

# Ler(read) e Escrever(write)
# with open("arquivo.txt", "w+") as f:
#     f.write("Texto novo")
#     f.seek(0)     # mover cursor para o início
#     print(f.read())

# Adicionar(a) e Ler(read)
with open("teste.txt", "a+") as f:
    f.write("Nova linha\n")
    f.write('Adicionando nova linha\n')
    f.seek(0)   # precisa reposicionar para ler
    print(f.read())

#Removendo arquivos(preciso dar 'import os')
    os.remove('teste.txt')
    