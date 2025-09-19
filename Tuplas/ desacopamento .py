# Desacopamento 

times = ['Santos','Flamengo','Corinthias','Vasco','Fluminense','Sao Paulo','Palmeiras']
try:
    times = ['Santos','Flamengo','Corinthias','Vasco','Fluminense','Sao Paulo','Palmeiras']

    time1, *_ = times #  " _ ": VARIAVEIL USADA SOMENTE PARA DECLARAR, USADA PARA DIZER A OUTROS DEVs QUE NAO É UTILIZADA
    print(time1)

except:
    print('Variaveis insuficientes para a quantidade de valor na lista')

# times = ['Santos','Flamengo','Corinthias','Vasco','Fluminense','Sao Paulo','Palmeiras']
# # times.sort()

# # print(times)



