custo = [1000,950,550,870,2000,350,750]

custo_ordenado = sorted(custo)# Funcao no python que ordena de forma crescente
custo_reversa = sorted(custo, reverse = True) # Funcao no python que ordena de forma decrescente

print(f'\n Lista de forma Crescente {custo_ordenado} \n')
print(f'Lista de forma Decrescente {custo_reversa}')