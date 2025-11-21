custo = [1000,950,550,870]

soma_de_custo = list(filter(lambda x: x  >= 1000, custo)) # filtrar com lambda onde os salarios sejam menores que 1000, usamos 'filter'
print(f'salario maior que 1000 é {soma_de_custo}')