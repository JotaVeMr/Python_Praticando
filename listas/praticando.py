times_futebol = ['Santos','Flamengo','Corinthias','Vasco','Fluminense','Sao Paulo','Palmeiras']

del (times_futebol[1])
times_futebol.insert(2,'Cruzeiro')


ultimo_deletado = times_futebol.pop()

print(f'Times adicionados na listas sao {times_futebol} e os excluidos foram {ultimo_deletado}')


#tamanho da minha lista

print(f'Tamanho da lista é {len(times_futebol)}, fora o(s) excluido(s) {ultimo_deletado}')