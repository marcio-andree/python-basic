tentativa = 0
while tentativa < 3:
  print('tentar novamente')
  tentativa += 1

# ########################################################################

# senha
senha = ''
while senha != '123456':
  senha = str(input('Digite sua senha: '))
print('Bem vindo')

# ########################################################################

nome = ''
while nome == '':
  nome = str(input('Digite seu nome: '))
print(f'Bem vindo {nome}')

########################################################################

# contador crescente
cont = 0
while cont < 100:
  print(cont)
  cont += 1

########################################################################

# contador decrescente
contador = 100

while contador >= 0:
  print(contador)
  contador -= 1

################################################################

# Crie um loop while que irá contar e imprimir de 1 até 120
cont = 1
while cont < 121:
  print(cont)
  cont += 1

# cria um loop while que irá continuar pedindo a
# senha para entrada e só irá permitir a entrada caso a digite a senha 'secreto'

senha = ''
while senha != 'secreto':
  senha = str(input('Digite sua senha: '))
print('Bem vindo senha correta')

# cria um loop while que irá imprimir na tela o valor em ordem descrente de 100 para 1
contador = 100
while contador >= 1:
  print(contador)
  contador -= 1
