def exibirPreco(*,produto, preco):
  print(f'{produto} está no valor de: {preco}')

# Argumento posicional
exibirPreco('iphone', 7000)
# Argumento nomeado
exibirPreco(preco=5000,produto='iphone')


def gerarObjetoPersonalizado(cor, *, altura, formato):
  return print(f'A cor é: {cor} , a altura é: {altura} ,o formato é: {formato}')


gerarObjetoPersonalizado('Azul', altura=170, formato='quadrado')
