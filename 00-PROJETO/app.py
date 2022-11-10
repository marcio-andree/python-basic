from datetime import datetime
import random
# obtenha nome ,idade do usuário e a data atual de forma automática
# exiba olá (nome do usuário), seu registro foi feito com sucesso no dia (data)
# parabéns,houve um sorteio e você ganhou um cartão de compras no valor de (valor sorteado)

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade:'))
data_cadastro = datetime.now()
cartoes = ['R$50,00','R$250,00','R$120,00']
cartao_sorteio = random.choice(cartoes)
aniversario = datetime.strptime(input('Digite sua data de aniversário nesse formato dd/mm/aaaa: '), '%d/%m/%Y')
print(f'Olá {nome}, seu registro foi concluido com sucesso no dia {data_cadastro.day}/ {data_cadastro.month}/ {data_cadastro.year}')
print(f'parabéns ,houve um sorteio e você ganhou um cartão de compras no valor de {cartao_sorteio}')
