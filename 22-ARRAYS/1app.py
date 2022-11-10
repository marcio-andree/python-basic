grupoG = ['brasil','servia','camarões', 'suiça']

# Exibe a posição item na lista
print(grupoG.index('suiça'))

# mostra o item da lista sem precisar de passar o número do índice dele
print(grupoG[grupoG.index('suiça')])


# Formas de criar uma lista
lista_de_noves = [9] * 10
print(lista_de_noves)

lista_teste = ['Flamengo'] * 10
print(lista_teste)

rangeNumber = list(range(20))
print(rangeNumber)


def geradorDeNumero():
  gerador = list(range(10, 21))
  return gerador

print(geradorDeNumero())

# criação de Matrizes
listaNomes = [['thor',8], ['sumer',0]]
print(listaNomes[0])
print(listaNomes[0][0])

