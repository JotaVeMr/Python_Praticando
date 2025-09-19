times_futebol = ['santos','corinthias','flamengo','palmeiras']
times_futebol.append('vasco')
del times_futebol[1]
ultimo_deletado = times_futebol.pop()

indice = range(len(times_futebol))

for i in indice:
    print(i,times_futebol[i])
    
print(f'ultimo deletado {ultimo_deletado}')