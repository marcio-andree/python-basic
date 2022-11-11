# Estamos extraindo preços de um site de produtos e queremos armazenar as informações encontradas
# porém a pesquisa foi encontrada em momentos diferentes, assim acabamos com duas listas diferentes, favor criar uma mensagem
# que diz o nome e valor do produto

# Produto: Produto 1 encontrado no valor de R$500,00
# Produto: Produto 2 encontrado no valor de R$1500,00
# Produto: Produto 3 encontrado no valor de R$2700,00
# Produto: Produto 4 encontrado no valor de R$500,00
# Produto: Produto 5 encontrado no valor de None

'''
asdfasdf
'''



from itertools import zip_longest

produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
precos = ['R$500,00', 'R$1500,00', 'R$2700,00', 'R$500,00']

for produto, precos in zip_longest(produtos,precos):
  print(f'Produto: {produto} encontrado no valor de {precos}')
