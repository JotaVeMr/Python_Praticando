custo = [1000,950,550,870,2000,350,750]
funcionarios = ['joao','claudio','andre','roberto','ferreiro','rochet','renata']

for i,custos in zip(funcionarios,custo):  
    print(f'funcionario {i} -> {custos}')


#print(zip(funcionarios,custo))