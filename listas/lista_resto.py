infos = [
    "Joao",
    "Vitor",
    "casado",
    "estudante",
    "jogador",
    "20 anos"  

]

nome, _,_,_,profissao, *_ = infos # SÓ PODE USAR (*_) UMA VEZ, CASO QUEIRA "PULAR" PARTE DA LISTA, UTILIZAMOS " _, _, "

print(f'Nome: {nome} \nProfissao: {profissao}')