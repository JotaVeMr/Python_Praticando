try:
    lista = ['Joao vitor', 'Renata', 'Andre']
    lista[0] = 'Joao'

    lista.append('Claudete') # funçao do python para Adicionar um indice(sempre no final da lista) um uma lista
    lista.append('Paulo')
    lista.append('Elaine')

    del lista[3] # funçao no python para Deletar um indice da lista no caso de 0 a o numero maximo de indice dentro da lista
 #  del lista[4]
    ultimo_valor_removido = lista.pop()  # Remove o Ultimo indice(elemento) de uma lista

    lista.insert(1,'Renata Adelina') # Quase a mesma coisa que o append, mas o insert pode inserir antes ou apos  incice que voce deseja¸
#    print(f'lista {lista}', ultimo_valor_removido)
    print(lista[10])
  #  lista.clear()
    

except IndexError:
    print('O número que voce quer acessar é maior que a quantidade da Lista ')
