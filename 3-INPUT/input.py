# recebendo dados do usuário com metodo input
# como padrão python transforma todos os inputs em strings

senha = input('Digite seu nome: ')
print(senha)
print(type(senha))

# para resolver esse problema é necessário converter o tipo de dados a ser inserido
senha_2 = int(input('Digite a sua senha:'))
print(senha_2)
print(type(senha_2))
