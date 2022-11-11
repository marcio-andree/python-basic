from itertools import zip_longest

# listaA = ['A', 'B', 'C', 'D', 'E']
# listaB = [1,2,3,4,5,6]

# for a, b in zip(listaA, listaB):
#   print(a,b)



# produtos = ['produto 1', 'produto 2', 'produto 3', 'produto 4', 'produto 5']
# precos = [200,100,300,450,500,800]
# for a, b in zip(produtos, precos):
#   print(f'Salvando produto {a} valor R$ {b}')


titulos = ['Titulo 1', 'Titulo 2', 'Titulo 3', 'Titulo 4']
descricoes = ['Descricao 1', 'Descricao 2', 'Descricao 3']

for titulo, descricao in zip_longest(titulos, descricoes):
  print(f'Encontramos o {titulo} descrição {descricao}')
