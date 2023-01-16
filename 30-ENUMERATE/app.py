# enumerate mostra o indice da iteração

# for index, numero in enumerate(range(1,10), 0):
#   print(f'Sou o index: {index}, sou a iteração: {numero}')
#   if index == 5:
#     print('estamos na metade da lista ')




listaFrutas = ['Maça', 'Laranja', 'Morango', 'Limão']

for index, frutas in enumerate (listaFrutas, 0):
  print(f' estou no index {index} fruta é {frutas}')
  if index == 3:
    print(f'estou no index {index} - fruta em promoção é {frutas}')

