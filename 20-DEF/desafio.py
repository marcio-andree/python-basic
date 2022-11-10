def nomeSobrenome(nome, sobrenome):

  nomeCompleto = nome, sobrenome
  return print(f'Bem-vindo {nomeCompleto}')



def calcularValores(preco_produto, quantidade=1):

  resultado = preco_produto * quantidade
  return print(f'O valor do produto é: {resultado}')



nomeSobrenome('Marcio Anré', 'Silva')
calcularValores(5, 2)
